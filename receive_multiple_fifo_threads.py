import boto3
import time
import threading
import logging

# Get the service resource
sqs = boto3.resource('sqs')

# Get the queue
queue = sqs.get_queue_by_name(QueueName='test.fifo')

# Num of messages to get
num_msg = 10

def get_messages_fast(name):
  for message in queue.receive_messages(MaxNumberOfMessages=10):
    logging.info("Thread %s - %s", name, message.body) # Print out the body of the message with thread id
    message.delete () # Let the queue know that the message is processed

def get_messages_slow(name):
  for message in queue.receive_messages(MaxNumberOfMessages=10):
    logging.info("Thread %s - %s", name, message.body) # Print out the body of the message with thread id
    time.sleep(1) # Sleep for a few to give the other threads a chance to attempt to get messages from queue
    message.delete () # Let the queue know that the message is processed

# Inspiration from https://realpython.com/intro-to-python-threading/
format = "%(asctime)s: %(message)s"
logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")
threads = list()
for index in range(5):
  logging.info("Main    : create and start thread %d.", index)
  x = threading.Thread(target=get_messages_slow, args=(index,))
  threads.append(x)
  x.start()

for index, thread in enumerate(threads):
  logging.info("Main    : before joining thread %d.", index)
  thread.join()
  logging.info("Main    : thread %d done", index)
