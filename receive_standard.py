import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test')

# Process messages by printing out body
for message in queue.receive_messages():
    # Print out the body of the message
    print(message.body)

    # Let the queue know that the message is processed
    message.delete()
