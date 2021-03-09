from painel import Painel

p = Painel('228.0.0.8',50000,'Painel','127.0.0.1',65432)

while True:
    p.receive_message()
