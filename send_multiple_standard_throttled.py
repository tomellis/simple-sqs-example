import boto3
import time

# Use Token Bucket Algorithm for Throttling of requests to SQS in order to limit overwhelming or overloading a downstream system by filling up the queue
class TokenBucket:

    def __init__(self, tokens, fill_rate):
        self.capacity = tokens
        self.fill_rate = fill_rate
        self.tokens = tokens
        self.last_check = time.time()

    def remove_token(self):
        now = time.time() 
        time_passed = now - self.last_check
        self.tokens += time_passed * self.fill_rate
        if self.tokens > self.capacity:
            self.tokens = self.capacity
        self.last_check = now
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        else:
            return False

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test')

# Define the token bucket size and refill rate
bucket = TokenBucket(10, 1) # 10 tokens, refill 1 per second

# Message Loop
my_seq = 1
while my_seq <= 100:
    if bucket.remove_token():
        # Send request
        my_message = 'This was message ' + str(my_seq) # Create a message
        response = queue.send_message(MessageBody=my_message) # Send the message
        print(response) # print the output
        my_seq = my_seq + 1 # Add to the loop sequence
    else:
        # Limit reached, do not send request
        print("Limit reached, throttling using token bucket algorithm")
        time.sleep(0.1)
