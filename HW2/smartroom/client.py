import socket
import app_pb2
class SmartRoomClient():
    def __init__(self,server_ip,server_port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((server_ip, server_port))
        
    
    def rec_mensage(self):
        mensagem=self.client_socket.recv(1024)
        response_object =app_pb2.Response()
        response_object.ParseFromString(mensagem)
        return response_object
    
    def send_mensage(self,mensagem_type,mensagem_object):
        request_mensage = app_pb2.Request()
        
        
        if mensagem_object == 'tv':
            request_mensage.gtype = app_pb2.Request.GType.TV
        
        if mensagem_object == 'ar':
            request_mensage.gtype = app_pb2.Request.GType.AR
        
        if mensagem_object == 'lamp':
            request_mensage.gtype = app_pb2.Request.GType.LAMPADA
        if mensagem_type == 'sensor':
            request_mensage.rtype = app_pb2.Request.RequestType.ReadSensor
        if mensagem_type == 'modstatus':
            request_mensage.rtype = app_pb2.Request.RequestType.ModStatus
        if mensagem_type == 'status':
            request_mensage.rtype = app_pb2.Request.RequestType.ReadStatus
        
        
        self.client_socket.send(request_mensage.SerializeToString())