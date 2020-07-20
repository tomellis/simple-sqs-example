import boto3
import time

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test.fifo')

# Num of messages to get
num_msg = 10

# Process messages by printing out body
for message in queue.receive_messages(MaxNumberOfMessages=num_msg):
    # Print out the body of the message
    print(message.body)
    time.sleep(2) # give me 2 seconds before deleting to test another receive worker
    # Let the queue know that the message is processed
    message.delete()
