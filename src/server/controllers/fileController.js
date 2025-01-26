import AWSService from '../services/AWSService.js';
import { validatePythonFiles, validateFileCount } from '../utils/validation.js';
import { unzipFile, zipFiles } from '../utils/zipUtils.js';
import fs from 'fs';
import path from 'path';

const awsService = new AWSService();

export const uploadFile = async (req, res) => {
    try {
        const { file } = req; // Assuming middleware like multer processes the file
        if (!file) return res.status(400).json({ error: 'No file uploaded.' });

        const tempDir = `temp-${Date.now()}`;
        fs.mkdirSync(tempDir);

        // Extract the zip file
        unzipFile(file.path, tempDir);

        const files = fs.readdirSync(tempDir);
        validateFileCount(files, 500);

        for (const filename of files) {
            const filePath = path.join(tempDir, filename);
            if (path.extname(filename) === '.py') {
                validatePythonFiles(filePath, 200);
            }
        }

        // Re-zip and upload to S3
        const outputZipPath = `compiled-${Date.now()}.zip`;
        zipFiles(tempDir, outputZipPath);
        const s3Key = await awsService.uploadToS3(outputZipPath);

        // Send message to SQS
        await awsService.sendMessageToSQS({
            s3Key,
            bucket: awsService.bucketName,
        });

        res.status(200).json({ message: 'File processed successfully.', s3Key });
    } catch (error) {
        console.error('Error:', error.message);
        res.status(500).json({ error: error.message });
    }
};
