# Multilevel inheritance


#inheritance

#parent / base class

class Bird:
    def __init__(self):
        print("Bird is ready....")

    def WhosThis(self):
        print("Bird")    
 
    def swim(self):
        print("Swim faster")
#child class
class Bird1(Bird):
    def __init__(self):
        print("Bird is ready....")

    def WhosThis1(self):
        print("Bird")    
 
    def swim1(self):
        print("Swim faster")  
#child class
class Bird2(Bird1):
    def __init__(self):
        print("Bird is ready....")

    def WhosThis2(self):
        print("Bird")    
 
    def swim2(self):
        print("Swim faster")               

#child class
class MyBird(Bird2):
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

childInstance=MyBird()

childInstance.WhosThis()
childInstance.swim()

# Bird1
childInstance.WhosThis1()
childInstance.swim1()

#Bird2
childInstance.WhosThis2()
childInstance.swim2()