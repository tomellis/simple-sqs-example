import boto3
import uuid

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test.fifo')

# Message group id
msg_group_id = 'messageGroup1'

# Generate a deduplication id
dedup_id = uuid.uuid4().hex
print('UUID for dedup: ' + dedup_id)

# Create a message
my_message = "Hello there"

# Send the message
response = queue.send_message(
    MessageBody=my_message,
    MessageGroupId=msg_group_id,
    MessageDeduplicationId=dedup_id
)

print(response)
