import math
import random
class Ponto:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def distancia(self,p1):
        return format(math.sqrt(math.pow((p1.x - self.x),2)+ (math.pow(p1.y-self.y),2)),".2f")
    def __repr__(self):
        return f'{self.x,self.y}'
def main():
    lst = random.sample(range(0,10),10)
    lst1 = []
    for i in range(4):
        lst1.append(Ponto(lst[i],lst[i+1]))
    for i in range(len(lst1)):
        for j in range(len(lst1)):
            if j==i:continue
            print(f"a distancia entre {lst1[i]} e {lst1[j]} é: {lst1[i].distancia(lst1[j])}")

if __name__=="__main__":
    main()