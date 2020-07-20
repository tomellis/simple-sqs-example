# Simple SQS Examples in Python

## Helper scripts

- purge_queues.py - purge all messages from test standard queue and test.fifo queue

## Standard Queues

- send_standard.py - send a single message to a standard queue
- receive_standard.py - receive a single message from the queue queue and delete it
- send_multiple_standard.py - send 1000 messages to a standard queue

## FIFO Queues

- send_fifo.py - send a single message to a fifo queue
- send_multiple_fifo.py
- receive_fifo.py - receive a single message from a fifo queue
- receive_multiple_fifo.py - receive a batch of 10 messages from a fifo queue and delete them
- send_multiple_standard.py - send 1000 messages all with the same group id
- send_fifo_dup.py - send a single message with a static duplication id, send this as many times as you like then run receive_fifo.py to see there is only one due to deduplication
- send_multiple_fifo_groupid.py - send 100 messages with the same group id then 20 more per group id, up to group id of 5. This loads one groupid more than others to experiement with.
- receive_multiple_fifo_delay.py - receive a batch of 10 messages from a fifo queue then wait 3 seconds before deleting them. Run this with another recieve_multiple_fifo.py in paralell to test behaviour of FIFO SQS.
- receive_multiple_fifo_threads.py - using 5 threads, receive a batch of 10 messages from a fifo queue waiting 2 seconds between batch before deleting them, demonstrating behaviour between threads/workers picking up messages.
