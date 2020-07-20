import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test.fifo')

# Generate a deduplication id
# Set a static dedup id that we can use to test dedupe of messages
dedup_id = '683bf4c4e9ba406db1f8ebb36d7a873e'

# Create a message
my_message = "Hello there"

# Send the message
response = queue.send_message(
    MessageBody=my_message,
    MessageGroupId='messageGroup1',
    MessageDeduplicationId=dedup_id
)

print(response)
