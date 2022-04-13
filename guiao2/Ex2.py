from ExternalClasses import *
import math
import turtle
import random
class Circle(Figure):
    def __init__(self, radio = 20):
        self.radio = radio
        super().__init__()
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

class Square(Figure):
    def __init__(self,_side) -> None:
        self.side = _side 
        super().__init__()
    def area(self):
        print(self.side**2)
    def preim(self):
        print(4*self.side)
    def getshape(self):
        t = turtle.Turtle()
        for _ in range(4):
            t.forward(self.side) # Forward turtle by s units
            t.left(90) # Turn turtle by 90 degree


class Figures: 
    def randShape(): 
        rn = random.randrange(0,2)
        size = random.randomrange(0,10)#just a line to create diferent shapes for the same figure, but the methods have default value so is possible to erase 
                                        #this line and the code works too
        if rn == 0: 
            return Circle(size)
        elif rn ==1: 
            return Square(size)

def main(): 
    figures = [] 
    for i in range(9): 
        figures.append(Figures.randShape())
    for fig in figures: 
        fig.area()