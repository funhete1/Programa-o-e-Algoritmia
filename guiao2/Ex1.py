class Vehicle:
    def __init__(self, max_speed, kilometers, color, brand, registration):
        self.ms = max_speed
        self.km = kilometers
        self.color = color
        self.brand = brand
        self.regs = registration
    def set_max_speed(self, max_sp):
        self.ms = max_sp
    def get_max_speed(self): # returns value of max_speed attribute
        return self.ms  
    def set_kilometers(self, kms):
        self.km = kms
    def get_kilometers(self): # returns value of kilometers attribute
        return self.km  

class ElectricVehicle(Vehicle):
    def __init__(self, max_speed, kilometers, color, brand, registration,ptotal,motors):
        self.ptotal = ptotal
        self.motors = motors
        super().__init__(max_speed, kilometers, color, brand, registration)
    def __repr__(self):
        return f"{self.regs} : {self.brand}, {self.color}, {self.ms}km/h. {self.km}km, {self.motors} motors, {self.ptotal}KW"
class CombustionVehicle(Vehicle):
    def __init__(self, max_speed, kilometers, color, brand, registration,ptotal):
        self.ptotal = ptotal
        super().__init__(max_speed, kilometers, color, brand, registration)
    def __repr__(self):
        return f"{self.regs} : {self.brand}, {self.color}, {self.ms}km/h. {self.km}km, {self.ptotal}cm3"

def main():
    v1 = ElectricVehicle(190,0,'black','Tesla',"DZ-59-27",100,1) 
    v2 = CombustionVehicle(310,0,'red','Ferrari',"OF-00-00",3000) 
    print(v1) 
    print(v2)
main()