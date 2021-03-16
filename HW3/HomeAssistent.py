import pika
from _thread import *
import threading 
import json

def callback_1(ch, method, properties, body):
    print("(Sensor 1) Received %r" % body)

def callback_2(ch, method, properties, body):
    print(" (Sensor 2)  %r" % body)
              
def listen_sensor_1(channel,queue_name):
    print("Thread 1")
    while True:
        channel.basic_consume(queue=queue_name, 
                        on_message_callback=callback_1, 
                        auto_ack=True)
        channel.start_consuming()

def listen_sensor_2(channel,queue_name):
    print("Thread 2")
    while True:
        channel.basic_consume(queue=queue_name, 
                        on_message_callback=callback_2, 
                        auto_ack=True)
        channel.start_consuming()
        
connection_1 = pika.BlockingConnection(pika.ConnectionParameters(host=
                                                                   'localhost'))
connection_2 = pika.BlockingConnection(pika.ConnectionParameters(host=
                                                                   'localhost'))
channel_1 = connection_1.channel()
channel_2 = connection_2.channel()

print("Iniciando a primeira thread")
t_1 = threading.Thread(target =listen_sensor_1,args=(channel_1,'sensor_1',))
t_2 = threading.Thread(target =listen_sensor_2,args=(channel_2,'sensor_2',))

t_1.start()
t_2.start()
