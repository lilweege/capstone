import os
import json
import shutil
from app.pipeline import CodeSimilarityPipeline
from config.aws_config import AWSConfig

TEMP_DIR = "data/temp"
RESULTS_DIR = "data/results"

def process_message(message, aws_config: AWSConfig, pipeline: CodeSimilarityPipeline):
    # Parse the SQS message
    body = json.loads(message["Body"])
    s3_key = body["s3Key"]

    # Download the zip file from S3
    local_zip_path = os.path.join(TEMP_DIR, os.path.basename(s3_key))
    aws_config.download_from_s3(s3_key, local_zip_path)

    # Extract the zip file
    extracted_dir = os.path.join(TEMP_DIR, "extracted")
    os.makedirs(extracted_dir, exist_ok=True)
    shutil.unpack_archive(local_zip_path, extracted_dir)

    # Read all Python file pairs
    file_pairs = []
    python_files = [os.path.join(extracted_dir, f) for f in os.listdir(extracted_dir) if f.endswith(".py")]
    for i in range(len(python_files)):
        for j in range(i + 1, len(python_files)):
            with open(python_files[i], "r") as f1, open(python_files[j], "r") as f2:
                code1 = f1.read()
                code2 = f2.read()
            file_pairs.append(((python_files[i], code1), (python_files[j], code2)))

    # Compute similarity for each pair
    results = []
    for (file1, code1), (file2, code2) in file_pairs:
        scores = pipeline.compute_all(code1, code2)
        results.append({"file1": file1, "file2": file2, **scores})

    # Save results to JSON
    results_path = os.path.join(RESULTS_DIR, f"results_{os.path.basename(s3_key)}.json")
    with open(results_path, "w") as f:
        json.dump(results, f, indent=4)

    # Upload results to S3
    s3_results_key = f"results/{os.path.basename(results_path)}"
    aws_config.upload_to_s3(results_path, s3_results_key)

    # Cleanup
    shutil.rmtree(TEMP_DIR)

    return s3_results_key

if __name__ == "__main__":
    aws_config = AWSConfig()
    pipeline = CodeSimilarityPipeline()

    os.makedirs(TEMP_DIR, exist_ok=True)
    os.makedirs(RESULTS_DIR, exist_ok=True)

    while True:
        messages = aws_config.receive_message()
        if not messages:
            print("No messages in queue.")
            continue

        for message in messages:
            receipt_handle = message["ReceiptHandle"]
            try:
                print("Processing message:", message["Body"])
                result_s3_key = process_message(message, aws_config, pipeline)
                print("Results uploaded to:", result_s3_key)

                # Delete the message from the queue
                aws_config.delete_message(receipt_handle)
            except Exception as e:
                print("Error processing message:", e)
