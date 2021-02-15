from televisao import Television
import gateway_pb2

tv = Television('228.0.0.8',50000,'Televisao','127.0.0.1',65432)

while True:    
    tv.receive_message()
