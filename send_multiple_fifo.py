import boto3
import uuid

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test.fifo')

# Message group id
msg_group_id = 'messageGroup1'

# Message Loop
my_seq = 1
while my_seq <= 1000:
  #print(my_seq)
  dedup_id = uuid.uuid4().hex # Generate a deduplication id
  my_message = 'This was message ' + str(my_seq) # Create a message
  response = queue.send_message(MessageBody=my_message,MessageGroupId=msg_group_id,MessageDeduplicationId=dedup_id) # Send the message
  print(response) # print the output
  my_seq = my_seq + 1 # Add to the loop sequence
