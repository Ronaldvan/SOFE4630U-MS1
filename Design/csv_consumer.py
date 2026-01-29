from google.cloud import pubsub_v1      # Pub/Sub client
import json
#import glob
#import os

# Using Application Default Credentials (ADC)
# Authenticated via: gcloud auth application-default login

# GCP configuration
project_id = "cloudcompprojectmilestone1"
subscription_id = "csvLabels-sub"

# Create subscriber
subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(project_id, subscription_id)

print(f"Listening on {subscription_path}...\n")

# Callback for received messages
def callback(message):
    record = json.loads(message.data.decode("utf-8"))
    print("Consumed record:")
    for key, value in record.items():
        print(f"  {key}: {value}")
    print("-" * 30)
    message.ack()

with subscriber:
    streaming_pull_future = subscriber.subscribe(subscription_path, callback=callback)
    try:
        streaming_pull_future.result()
    except KeyboardInterrupt:
        streaming_pull_future.cancel()
