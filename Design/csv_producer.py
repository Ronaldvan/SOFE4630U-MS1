from google.cloud import pubsub_v1      # Pub/Sub client
import csv                              # CSV reader
import json                             # Serialization
#import glob                             # Locate JSON key
#import os

# Locate service account key
#files = glob.glob("*.json")
#os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = files[0]

# GCP configuration
project_id = "cloudcompprojectmilestone1"
topic_name = "csvLabels"

# Create publisher
publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(project_id, topic_name)

print(f"Publishing CSV records to {topic_path}")

# Read CSV and publish each row
with open("Labels.csv", newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        message_data = json.dumps(row).encode("utf-8")
        future = publisher.publish(topic_path, message_data)
        future.result()
        print("Published:", row)
