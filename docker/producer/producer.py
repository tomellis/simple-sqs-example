import boto3
import uuid

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test.fifo')

msg_group_id = 1
while msg_group_id <= 5:
    my_seq = 1
    while my_seq <= 100:
        dedup_id = uuid.uuid4().hex # Generate a deduplication id
        my_message = 'This was message ' + str(my_seq) + ' with group_id ' + str(msg_group_id) # Create a message
        print(my_message)
        response = queue.send_message(MessageBody=my_message,MessageGroupId=str(msg_group_id),MessageDeduplicationId=dedup_id) # Send the message
        print(response)
        my_seq+=1
    msg_group_id+=1
