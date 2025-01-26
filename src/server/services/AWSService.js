import AWS from 'aws-sdk';
import fs from 'fs';

class AWSService {
    constructor() {
        AWS.config.update({ region: process.env.AWS_REGION });
        this.s3 = new AWS.S3();
        this.sqs = new AWS.SQS();
        this.bucketName = process.env.S3_BUCKET_NAME;
        this.queueUrl = process.env.SQS_URL;
    }

    async uploadToS3(filePath) {
        const fileName = filePath.split('/').pop();
        const fileStream = fs.createReadStream(filePath);

        const params = {
            Bucket: this.bucketName,
            Key: `uploads/${fileName}`,
            Body: fileStream,
        };

        const result = await this.s3.upload(params).promise();
        return result.Key;
    }

    async sendMessageToSQS(messageBody) {
        const params = {
            QueueUrl: this.queueUrl,
            MessageBody: JSON.stringify(messageBody),
        };

        await this.sqs.sendMessage(params).promise();
    }
}

module.exports = AWSService;
