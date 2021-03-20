import pika
import socket
import EnvMsg_pb2
import HAmsg_pb2

class Sensor():
    
    def __init__(self,ambiente_ip,ambiente_port,sensor_type,sensor_name):
        connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
        self.channel = connection.channel()
        self.channel.queue_declare(queue=sensor_name)
        self.sensor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sensor_socket.connect((ambiente_ip,ambiente_port))
        
        msg = EnvMsg_pb2.FromSensor()
        msg.type = sensor_type
        msg.queue_name = sensor_name
        self.sensor_name = sensor_name
        self.sensor_socket.send(msg.SerializeToString())
        self.variable = -1
        self.old_variable=-1        
    
    def publish(self):
        if self.variable!=-1:
            if self.variable!=self.old_variable or self.variable==-1:
                self.old_variable = self.variable
                self.channel.basic_publish(exchange='', 
                              routing_key=self.sensor_name, 
                              body=f'{self.variable}'
                              )
    def get_data(self):
        messagem_env = EnvMsg_pb2.ToSensor()
        messagem_env.ParseFromString(self.sensor_socket.recv(1024))    
        self.variable = messagem_env.variable
    