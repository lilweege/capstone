import express from "express";
import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { spawn } from "child_process";
import nodemailer from "nodemailer";
import archiver from "archiver";
import multer from "multer";

// Import your environment, logger, and custom exceptions
import { EmailVariables, AuthVariables } from "../constants/envConstants.js";
import logger from "../utilities/loggerUtils.js";
import {
  BadRequestException,
  HttpRequestException,
} from "../types/exceptions.js";

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const templatePath = path.join(
  __dirname,
  "..",
  "templates",
  "similarityResultsTemplate.html"
);

const router = express.Router();
export default router;

// Configure Nodemailer
const transporter = nodemailer.createTransport({
  service: "gmail",
  auth: {
    user: EmailVariables.EMAIL_USER,
    pass: EmailVariables.EMAIL_PASS,
  },
});

router.post("/", multer().any(), async (req, res, next) => {
  try {
    const token = req.headers.authorization.split(" ")[1];
    const response = await fetch(
      `https://${AuthVariables.AUTH0_DOMAIN}/userinfo`,
      {
        headers: {
          Authorization: `Bearer ${token}`,
        },
      }
    );
    const data = await response.json();
    const userEmail = data.email;

    if (!userEmail) {
      logger.warn("No email claim found in the Auth0 token payload");
      throw new BadRequestException(
        "No email claim found in token payload.",
        "NO_EMAIL_CLAIM"
      );
    }


    const analysisName = req.body.analysisName;

    const uploadDir = path.join(__dirname, "..", "files");
    if (!fs.existsSync(uploadDir)) {
      fs.mkdirSync(uploadDir, { recursive: true });
      logger.info(`Created directory: ${uploadDir}`);
    }

    if (!req.files || !Array.isArray(req.files) || req.files.length === 0) {
      logger.warn("No files found in request");
      throw new BadRequestException("No files uploaded.", "NO_FILES_UPLOADED");
    }

    req.files.forEach((file) => {
      const filePath = path.join(uploadDir, file.originalname);
      fs.writeFileSync(filePath, file.buffer);
      logger.info(`File written: ${filePath}`);
    });

    const pythonScriptPath = path.join(__dirname, "../..", "test.py");
    logger.info(`Spawning Python script at ${pythonScriptPath}`);

    const pythonProcess = spawn("python", [pythonScriptPath]);

    pythonProcess.stdout.on("data", (data) => {
      logger.info(`Python stdout: ${data}`);
    });

    pythonProcess.stderr.on("data", (data) => {
      logger.error(`Python stderr: ${data}`);
    });

    pythonProcess.on("close", async (code) => {
      logger.info(`Python script exited with code ${code}`);

      if (code !== 0) {
        return next(
          new HttpRequestException(
            500,
            `Python script failed with exit code ${code}`,
            "PYTHON_SCRIPT_ERROR"
          )
        );
      }

      try {
        const zipPath = path.join(__dirname, "../..", `${analysisName}.zip`);
        const output = fs.createWriteStream(zipPath);
        const archive = archiver("zip", { zlib: { level: 9 } });

        archive.pipe(output);

        const resultsJsonPath = path.join(
          __dirname,
          "../..",
          "similarity_results.json"
        );
        if (fs.existsSync(resultsJsonPath)) {
          archive.append(fs.createReadStream(resultsJsonPath), {
            name: "similarity_results.json",
          });
        } else {
          logger.warn("similarity_results.json not found. Skipping in zip.");
        }

        archive.finalize();

        // If archiver encounters an error, pass it to Express
        archive.on("error", (err) => {
          logger.error("Error creating zip archive:", err);
          return next(
            new HttpRequestException(500, err.message, "ZIP_CREATION_ERROR")
          );
        });

        // Once the zip is finalized, send the email
        archive.on("close", async () => {
          logger.info(
            `Zip file created at ${zipPath} with ${archive.pointer()} bytes.`
          );

          // Cleanup uploaded files
          req.files.forEach((file) => {
            const filePath = path.join(uploadDir, file.originalname);
            fs.unlink(filePath, (err) => {
              if (err) {
                logger.error(`Error deleting file ${filePath}: ${err.message}`);
              } else {
                logger.info(`File deleted: ${filePath}`);
              }
            });
          });

          // Send the email
          try {
            const info = await transporter.sendMail({
              from: '"Syntax Sentinels" <syntaxsentinals@gmail.com>',
              to: userEmail,
              subject: "SyntaxSentinels: Analysis Report",
              html: fs.readFileSync(templatePath, "utf8"),
              attachments: [
                {
                  filename: `${analysisName}.zip`,
                  path: zipPath,
                },
              ],
            });

            logger.info(
              `Email sent successfully to ${userEmail}: ${info.messageId}`
            );

            // Delete the zip file and results JSON
            fs.unlink(zipPath, (err) => {
              if (err) {
                logger.error(`Error deleting file ${zipPath}: ${err.message}`);
              } else {
                logger.info(`File deleted: ${zipPath}`);
              }
            });

            fs.unlink(resultsJsonPath, (err) => {
              if (err) {
                logger.error(
                  `Error deleting file ${resultsJsonPath}: ${err.message}`
                );
              } else {
                logger.info(`File deleted: ${resultsJsonPath}`);
              }
            });

            return res.json({
              message: "Email sent successfully!",
              info,
            });
          } catch (err) {
            logger.error("Error sending email:", err);
            return next(
              new HttpRequestException(500, err.message, "EMAIL_SENDING_ERROR")
            );
          }
        });
      } catch (err) {
        logger.error("Error while zipping or emailing:", err);
        // delete temp files
        req.files.forEach((file) => {
          const filePath = path.join(uploadDir, file.originalname);
          fs.unlink(filePath, (err) => {
            if (err) {
              logger.error(`Error deleting file ${filePath}: ${err.message}`);
            } else {
              logger.info(`File deleted: ${filePath}`);
            }
          });
        });
        return next(
          new HttpRequestException(500, err.message, "POST_PROCESSING_ERROR")
        );
      }
    });
  } catch (error) {
    next(error);
  }
});
