import pika
import sys


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# make queue durable
channel.queue_declare(queue='task_queue', durable=True)

message = " ".join(sys.argv[1:]) or 'Hello World'

for i in range(0, 10):
    channel.basic_publish(exchange='',
                          routing_key='task_queue',
                          body=message + '{}'.format(i),
                          properties=pika.BasicProperties(
                              delivery_mode=2  # make message persistent
                          ))
