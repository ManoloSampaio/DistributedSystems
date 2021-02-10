from televisao import Televisao
import gateway_pb2
tv = Televisao('228.0.0.8',60000,'Televisao','127.0.0.1','70000')
while True:
    mensage = tv.multicastsocket.recv(1024)
    print(mensage)
    tv.recieve_gateway(mensage)
    