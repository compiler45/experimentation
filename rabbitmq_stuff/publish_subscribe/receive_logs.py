import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',
                         exchange_type='direct')

# make queue durable
result = channel.queue_declare(exclusive=True)  # let server create queue for us
channel.queue_bind(exchange='direct_logs',
                   queue=result.method.queue)


print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] Received {}".format(body))


channel.basic_consume(callback,
                      queue='',
                      no_ack=True)  # no_ack=True to stop workers acknowledging messages

channel.start_consuming()
