from google.cloud import pubsub_v1

PROJECT_ID = "cloudcompprojectmilestone1"
SUBSCRIPTION_ID = "testTopic-sub"

subscriber = pubsub_v1.SubscriberClient()
subscription_path = subscriber.subscription_path(
    PROJECT_ID, SUBSCRIPTION_ID
)

def callback(message):
    print("Received:", message.data.decode("utf-8"))
    message.ack()

print(f"Listening on {subscription_path}...")
subscriber.subscribe(subscription_path, callback=callback)

input("Press Enter to stop listening...\n")
