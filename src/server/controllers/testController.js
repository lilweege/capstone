import fs from "fs";
import path from "path";
import { fileURLToPath } from "url";
import { spawn } from "child_process";
import nodemailer from "nodemailer";
import archiver from "archiver";
import { arch } from "os";
import { EmailVariables } from "../constants/envConstants.js";

// Define __filename and __dirname for ES modules
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const transporter = nodemailer.createTransport({
  service: "gmail", // You can use other services like Outlook, SMTP, etc.
  auth: {
    user: EmailVariables.EMAIL_USER,
    pass: EmailVariables.EMAIL_PASS,
  },
});

export const test = (req, res) => {
  const uploadDir = path.join(__dirname, "..", "files");

  const userClaims = req.auth.payload;

  // Example: Extract the Auth0 user ID (subject)
  const userId = userClaims.sub;

  // Ensure the upload directory exists
  if (!fs.existsSync(uploadDir)) {
    fs.mkdirSync(uploadDir, { recursive: true });
  }

  req.files.forEach((file) => {
    const filePath = path.join(uploadDir, file.originalname);
    fs.writeFileSync(filePath, file.buffer);
  });

  const pythonProcess = spawn("python", [
    path.join(__dirname, "../..", "test.py"),
  ]);

  pythonProcess.stdout.on("data", (data) => {
    console.log(`stdout: ${data}`);
  });

  pythonProcess.stderr.on("data", (data) => {
    console.error(`stderr: ${data}`);
  });

  pythonProcess.on("close", async (code) => {
    console.log(`Python script exited with code ${code}`);

    // Create a zip file of the similarity results
    const output = fs.createWriteStream(
      path.join(__dirname, "../..", "similarity_results.zip")
    );
    const archive = archiver("zip", {
      zlib: { level: 9 }, // Sets the compression level
    });

    archive.pipe(output);
    archive.append(
      fs.createReadStream(
        path.join(__dirname, "../..", "similarity_results.json")
      ),
      { name: "similarity_results.json" }
    );

    /*

    output.on('close', async () => {
      console.log(`Zip file created with ${archive.pointer()} total bytes`);

      // Clean up the files after the Python script completes
      req.files.forEach(file => {
        const filePath = path.join(uploadDir, file.originalname);
        fs.unlink(filePath, (err) => {
          if (err) {
            console.error(`Error deleting file ${filePath}:`, err);
          } else {
            console.log(`File ${filePath} deleted successfully`);
          }
        });
      });

      try {
        const info = await transporter.sendMail({
          from: '"Syntax Sentinals" <syntaxsentinals@gmail.com>',
          to: "mmohsink606@gmail.com",
          subject: "Similarity Results",
          text: "Please find the similarity results attached.",
          attachments: [
            {
              filename: 'similarity_results.zip',
              path: path.join(__dirname, '../..', 'similarity_results.zip')
            }
          ]
        });

        res.json({ message: 'Email sent!', info });

        archive.finalize();
      } catch (error) {
        console.error('Error sending email:', error);
        res.status(500).json({ error: error.message });
      }
    });

    archive.on('error', (err) => {
      throw err;
    });

    */

    archive.finalize();

    archive.on("close", async () => {
      console.log(`Zip file created with ${archive.pointer()} total bytes`);

      // Clean up the files after the Python script completes
      req.files.forEach((file) => {
        const filePath = path.join(uploadDir, file.originalname);
        fs.unlink(filePath, (err) => {
          if (err) {
            console.error(`Error deleting file ${filePath}:`, err);
          } else {
            console.log(`File ${filePath} deleted successfully`);
          }
        });
      });

      try {
        const info = await transporter.sendMail({
          from: '"Syntax Sentinals" <syntaxsentinals@gmail.com>',
          to: "mmohsink606@gmail.com",
          subject: "Similarity Results",
          text: "Please find the similarity results attached.",
          attachments: [
            {
              filename: "similarity_results.zip",
              path: path.join(__dirname, "../..", "similarity_results.zip"),
            },
          ],
        });

        res.json({ message: "Email sent!", info });
      } catch (error) {
        console.error("Error sending email:", error);
        res.status(500).json({ error: error.message });
      }
    });
  });
};
