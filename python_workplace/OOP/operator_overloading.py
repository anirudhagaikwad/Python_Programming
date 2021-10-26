class Complex:
    # defining init method for class
    def __init__(self, r, i):
        self.real = r
        self.img = i

    # overloading the add operator using special function
    def __add__(self, sec):
        r = self.real + sec.real
        i = self.img + sec.img
        return complx(r,i)

    # string function to print object of Complex class
    def __str__(self):
        return str(self.real)+' + '+str(self.img)+'i'

c1 = Complex(5,3)
c2 = Complex(2,4)
print("sum = ",c1+c2)