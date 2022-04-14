from Ex3 import Ponto
import math
import turtle
class Circle:
    def __init__(self,_color,_center,_radio):
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
    def __setradio__(self,_radio):
        self.radio = _radio
    def __setcenter__(self,_center):
        self.center = _center
    def getarea(self):
        return format(math.pi * self.radio**2,".2f")
    def getperim(self):
        return format(2*math.pi*self.radio,".2f")
    def getshape(self):
        t = turtle.Turtle()
        t.color(self.color)
        t.circle(self.radio)
    def intersect(self,c2):
        return math.hypot(self.center.x-c2.center.x, self.center.y-c2.center.y) <= (self.radio + c2.radio);
class Retangle:
    def __init__(self,__color,__center,__length,__width):
        self.color = __color
        self.center = __center
        self.length = __length
        self.width = __width
    def __getcolor__(self):
        return self.color
    def __getcenter__(self):
        return self.center
    def __getsides__(self):
        return (self.length,self.width)
    def __setcenter__(self,_center):
        self.center = _center
    def __setcolor__(self,_color):
        self.color = _color
    def __setsides__(self,_length,_width):
        self.length = _length
        self.width = _width
    def getarea(self):
        return self.length*self.width
    def getperim(self):
        return (2*self.length)+(2*self.width)
    def getshape(self):
        t = turtle.Turtle()
        t.forward(self.length)
        t.left(90) 
        # drawing second side
        t.forward(self.width) 
        t.left(90) 
        # drawing third side
        t.forward(self.length) 
        t.left(90) 
        # drawing fourth side
        t.forward(self.width) 
        t.left(90) 

class Square:
    def __init__(self,__center,__color,__side) -> None:
        self.color = __color
        self.center = __center
        self.side = __side 
    def __getcolor__(self):
        return self.color
    def __getcenter__(self):
        return self.center
    def __getside__(self):
        return self.side
    def __setcenter__(self,__center):
        self.center = __center
    def __setcolor__(self,__color):
        self.color = __color
    def __setsides__(self,__side):
        self.side = __side
    def getarea(self):
        return self.side**2
    def gtepreim(self):
        return 4*self.side
    def getshape(self):
        t = turtle.Turtle()
        for _ in range(4):
            t.forward(self.side) # Forward turtle by s units
            t.left(90) # Turn turtle by 90 degree

def main():
    #uncoment to teste the circle class:
    #"""
    center = Ponto(0,0)
    c1 =  Circle("red",center,50)
    print(f"Cor do circulo: {c1.__getcolor__()}")
    print(f"centro do circulo: {c1.__getcenter__()}")
    print(f"raio do circulo: {c1.__getradio__()}")
    c1.__setcolor__("blue")
    print(f"Nova cor do circulo: {c1.__getcolor__()}")
    c1.__setcenter__(Ponto(1,1))
    print(f"Novo centro do circulo: {c1.__getcenter__()}")
    c1.__setradio__(55)
    print(f"Novo raio do circulo: {c1.__getradio__()}")
    print(f"Area do circulo: {c1.getarea()}")
    print(f"Perimetro do circulo: {c1.getperim()}")
    print(f"Shape of the circle: {c1.getshape()}")
    c2 = Circle("black",Ponto(0,0),30)
    print(f"c1 and c2 intersect ? {c1.intersect(c2)}")
    #"""
    #the test for the other class is similar

if __name__=="__main__":
    main()