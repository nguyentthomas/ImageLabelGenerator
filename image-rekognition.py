import boto3
import os
from dotenv import load_dotenv
load_dotenv()

rekognition = boto3.client('rekognition')

response = rekognition.detect_labels(
    Image={'S3Object': {'Bucket': (os.getenv("BUCKET_NAME")), 'Name': (os.getenv("IMAGE_NAME"))}},
    MaxLabels=10
)

for label in response['Labels']:
    with open("output.txt", "a") as output:
        print(f"Label: {label['Name']}, Confidence: {label['Confidence']:.2f}%", file = output)
