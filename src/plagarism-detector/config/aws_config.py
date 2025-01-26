import boto3
import os
from dotenv import load_dotenv

load_dotenv()

class AWSConfig:
    def __init__(self, region="us-east-1"):
        self.s3 = boto3.client("s3", region_name=region)
        self.sqs = boto3.client("sqs", region_name=region)
        self.bucket_name = os.getenv("S3_BUCKET_NAME")
        self.queue_url = os.getenv("SQS_URL")

    def download_from_s3(self, s3_key, download_path):
        """Download a file from S3."""
        self.s3.download_file(self.bucket_name, s3_key, download_path)

    def upload_to_s3(self, local_path, s3_key):
        """Upload a file to S3."""
        self.s3.upload_file(local_path, self.bucket_name, s3_key)

    def receive_message(self):
        """Receive a message from the SQS queue."""
        response = self.sqs.receive_message(
            QueueUrl=self.queue_url,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=10,
        )
        return response.get("Messages", [])

    def delete_message(self, receipt_handle):
        """Delete a processed message from the SQS queue."""
        self.sqs.delete_message(QueueUrl=self.queue_url, ReceiptHandle=receipt_handle)
