from televisao import Televisao
import gateway_pb2
def recieve_mensage():
    response = gateway_pb2.Response()
    request = gateway_pb2.Request()
    request.ParseFromString(tv.socket.recv(1024))
    print(request)
    if request.rtype == 2:
        tv.volume = request.status
        print("Aqui")
    response.result = tv.volume
    tv.socket.send(response)     
        
tv = Televisao('228.0.0.8',50000,'Televisao','127.0.0.1',65432)
mensage = tv.multicastsocket.recv(1024)
tv.recieve_gateway(mensage)
print(mensage)
while True:    
    recieve_mensage()