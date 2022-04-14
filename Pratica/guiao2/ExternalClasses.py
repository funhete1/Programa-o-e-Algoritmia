import math
class Ponto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distancia(self,p1):
        return format(math.sqrt(math.pow((p1.x - self.x),2)+ (math.pow(p1.y-self.y),2)),".2f")
    def __repr__(self):
        return f'{self.x,self.y}'

class Figure:
    def __init__(self,_color = "black",_center = Ponto(0,0),_radio = 10):
        self.color = _color
        self.center = _center
        self.radio = _radio
    def __getcolor__(self):
        return self.color
    def __getcenter__(self):
        return self.center
    def __getradio__(self):
        return self.radio
    def __setcolor__(self,_color):
        self.color = _color