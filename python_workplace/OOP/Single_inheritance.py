# Single inheritance

#parent / base class

class Bird:
    def __init__(self):
        print("Bird is ready....")

    def WhosThis(self):
        print("Bird")    
 
    def swim(self):
        print("Swim faster")

#child class
class Penguin(Bird):
    def __init__(self):
        super().__init__()
        print("Penguin is ready...")

    def WhosThis(self):
        print("Bird Penguin...")

    def WhosThis(self,name,age):
        self.name=name
        self.age=age
        print("Bird Penguin...",self.name,self.age)    


objBird= Bird()
objBird.WhosThis()
objBird.swim()

childInstance=Penguin()

childInstance.WhosThis()
childInstance.swim()