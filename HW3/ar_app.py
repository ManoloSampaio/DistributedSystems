from arcon import ArCodicionado
import time
ar = ArCodicionado('ar1','localhost',52000,40000)
while True:
    time.sleep(3)
    ar.send_temperature()