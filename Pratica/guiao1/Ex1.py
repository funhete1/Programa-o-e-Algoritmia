class Vehicle:
    def __init__(self, max_speed, kilometers):
        self.ms = max_speed
        self.km = kilometers
    def set_max_speed(self, max_sp):
        self.ms = max_sp
    def get_max_speed(self): # returns value of max_speed attribute
        return self.ms  
    def set_kilometers(self, kms):
        self.km = kms
    def get_kilometers(self): # returns value of kilometers attribute
        return self.km

modelX = Vehicle(240, 18)
print(modelX.ms, modelX.km)
modelX.set_kilometers(1000)
modelX.set_max_speed(200)
print(f"Vehicle has {modelX.km} Km and a max speed of {modelX.ms} Kms/h")
