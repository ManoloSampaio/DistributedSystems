from televisao import Televisao
import gateway_pb2
def recieve_mensage():
    response = gateway_pb2.Response()
    request = gateway_pb2.Request()
    request.ParseFromString(tv.socket.recv(1024))
    print(request)
    if request.rtype == 2:
        tv.volume = request.status
        response.result =f'Volume da TV:{tv.volume}'
    if request.rtype == 0:
        response.result =f'Volume da TV:{tv.volume}'
    if request.rtype == 3:
        tv.ON_OFF = 'OFF'
        response.result =f'Agora A TV esta: {tv.ON_OFF}' 
        
tv = Televisao('228.0.0.8',50000,'Televisao','127.0.0.1',65432)

while True:    
    recieve_mensage()
