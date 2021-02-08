from dispositivo import Gadgets

class ArCodicionado(Gadgets):
    
    def __init__(self):
        super.__init__()
        self.temperature_set = 20
        self.temperature_sensor = 25
    
    def set_temperature(self,temperature):
        self.temperature_set = temperature
    
    def change_temperature(self):
        if self.temperature_sensor>self.temperature_set:
            self.temperature_sensor = self.temperature_sensor-0.1
        if self.temperature_sensor<self.temperature_set:
            self.temperature_sensor = self.temperature_sensor+0.1
    
    def see_temperature(self):
        return self.temperature_sensor
    