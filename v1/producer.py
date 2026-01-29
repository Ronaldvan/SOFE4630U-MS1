from google.cloud import pubsub_v1

# MUST match your GCP project ID exactly
PROJECT_ID = "cloudcompprojectmilestone1"
TOPIC_ID = "testTopic"

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path(PROJECT_ID, TOPIC_ID)

print(f"Publishing to {topic_path}")

while True:
    message = input("Enter a value (String): ")
    if message == "":
        break

    data = message.encode("utf-8")
    future = publisher.publish(topic_path, data)
    future.result()  # wait for confirmation
    print("Message published successfully.")
