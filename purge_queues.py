import boto3

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test')
# Purge all messages in queue
response = queue.purge()
print(response)
# Get the queue
queue = sqs.get_queue_by_name(QueueName='test.fifo')
# Purge all messages in queue
response = queue.purge()
print(response)
