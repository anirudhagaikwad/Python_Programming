# Encapsulation

class Laptop:
    def __init__(self):
        self.__maxprice=52000

    def sell(self):
        print("Selling price: {}".format(self.__maxprice))

    def setMaxPrice(self,price):
        self.__maxprice=price

l1=Laptop()
l1.sell()

# change price
l1.__maxprice=88000
l1.sell()

l1.setMaxPrice(68000)
l1.sell()
