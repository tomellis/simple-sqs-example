import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test')

# Create a message
my_message = "Hello there"

# Send the message
response = queue.send_message(
    MessageBody=my_message
)

print(response)
