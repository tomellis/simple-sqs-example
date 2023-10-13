import boto3
from limiter import get_limiter, limit

# Use Token Bucket Algorithm for Throttling of requests to SQS in order to limit overwhelming or overloading a downstream system by filling up the queue
# This example uses an external module called limiter to provide this functionality

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test')

limiter = get_limiter(rate=1, capacity=10)

# Message Loop
my_seq = 1

# Define the token bucket size and refill rate, 10 tokens, refill 1 per second
@limit(limiter)
def send_my_message(my_seq):
    my_message = 'This was message ' + str(my_seq) # Create a message
    response = queue.send_message(MessageBody=my_message) # Send the message
    print(response)

while my_seq <= 1000:
  send_my_message(my_seq)
  my_seq = my_seq + 1 # Add to the loop sequence
