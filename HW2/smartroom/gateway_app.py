from gateway import Gateway
from _thread import *
import threading 
import app_pb2

def add_app_users(gateway):
    while True:
        connection,adress=gateway.server_socket.accept()
        start_new_thread(listen_app_users,(connection,))

def listen_app_users(connection):
    while True:
        mensagem=connection.recv(1024)
        user_request = app_pb2.Request()
        user_request.ParseFromString(mensagem)
        server_response = app_pb2.Response()
        
        if user_request.rtype==0:
            
            status_mensage = gateway.get_status(user_request.gtype)
            server_response.status_value,server_response.object_name = status_mensage    
        
        if user_request.rtype==1:
            sensor_value,sensor_name = gateway.ReadSensor()
            server_response.sensor = sensor_value
            server_response.object_name=sensor_name 
       
        if user_request.rtype==2:
            new_status=user_request.status_modification
            gateway.send_status(new_status,user_request.gtype)
            server_response.status_value,server_response.object_name = gateway.get_status(user_request.gtype)
                   
        if user_request.rtype==3:
            if user_request.on_off==1:
                server_response.on_off=gateway.set_on(user_request.gtype)
            else:
                server_response.on_off=gateway.set_off(user_request.gtype)

            
        connection.send(server_response.SerializeToString())
        



print("Adicionando Users:")
gateway = Gateway('127.0.0.1','60000')

gateway.server_socket.bind(('127.0.0.1',65432))
gateway.server_socket.listen(1)

t_1 = threading.Thread(target = add_app_users(gateway))

t_1.start()
            