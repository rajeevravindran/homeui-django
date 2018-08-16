#!/usr/bin/env python
import pika,os

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()


channel.queue_declare(queue='alarm')

def alarm(ch, method, properties, body):
    """
    Execute the alarm script
    :param ch:
    :param method:
    :param properties:
    :param body:
    :return:
    """
    print(" [x] Received %r" % body)
    os.system(body)

channel.basic_consume(alarm,
                      queue='alarm',
                      no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()