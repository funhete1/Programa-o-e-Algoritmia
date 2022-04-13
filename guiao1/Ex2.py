class Complex:
    """Class represents a complex number."""
    def init(self, real, imaginary):
        """Initialize Complex class's attributes."""
        self.real = real
        self.imaginary = imaginary
    def repr(self):
        """Return string representation for repr()."""
        return (f'({self.real}' + (' + ' if self.imaginary >= 0 else ' - ') + f'{abs(self.imaginary)}i)')
    def add(self,complex1):
        c2 = Complex(self.real+complex1.real,self.imaginary+complex1.imaginary)
        return c2.repr()
    def subtract(self,complex1):
        c2 = Complex(self.real-complex1.real,self.imaginary-complex1.imaginary)
        return c2.repr()
    def multiply(self,c1):
        c2 = Complex(self.real*c1.real+(-1)*(self.imaginary*c1.imaginary), self.real*c1.imaginary + self.imaginary*c1.real)
        return c2._repr_()

    
#Area used to test da Complex class
"""
cmplx1= Complex(1,4)
cmplx2= Complex(5,1)
print(cmplx1)
print(cmplx2)
print(cmplx1.add(cmplx2))
print(cmplx1.subtract(cmplx2))
print(f"{cmplx1} + {cmplx2} = {cmplx1.add(cmplx2)}")
print(f"{cmplx2} + {cmplx1} = {cmplx2.add(cmplx1)}")
print(f"{cmplx1} - {cmplx2} = {cmplx1.subtract(cmplx2)}")
print(f"{cmplx2} - {cmplx1} = {cmplx2.subtract(cmplx1)}")
print(f"{cmplx1} * {cmplx2} = {cmplx1.multiply(cmplx2)}")
"""

def main():
    mulAllCombinatios()

def mulAllCombinatios():
    lst = [(1,2),(2,3),(3,4)]
    for i in range(len(lst)):
        lst[i] = Complex(lst[i][0], lst[i][1])
    for i in range(len(lst)):
        for j in range(len(lst)):
            if j==i:continue
            print(f"{lst[i]} * {lst[j]} = {lst[i].multiply(lst[j])}")
if __name__=="__main__":
    main()
