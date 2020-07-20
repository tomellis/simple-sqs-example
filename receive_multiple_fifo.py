import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test.fifo')

# Num of messages to get
num_msg = 10

# Process messages by printing out body
for message in queue.receive_messages(MaxNumberOfMessages=10):
    # Print out the body of the message
    print(message.body)

    # Let the queue know that the message is processed
    message.delete()
