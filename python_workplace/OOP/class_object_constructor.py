# Class,object,constructor,method

class Parrot:
    #class attribute
    species="bird"

# instance attribute / Constructor
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def sing(self,song):
        return "{} singns {}".format(self.name,song) 

    def dance(self):
        return "{} is now dancing..".format(self.name) 


# instance parrot class
        
tig=input("Enter bird name:: "  )
tigage=int(input("Enter bird age:: "  ))
blu=Parrot(tig,tigage)
fi=Parrot("fi",15)

print("blu object name :: ",blu.name)
print("blu object age :: ",blu.age)
#obj=Parrot() # object

# access class attributes
print("Blu is {}".format(blu.__class__.species))
print("fi is {}".format(fi.__class__.species))

#call instance method

print(blu.sing("hello"))
print(blu.dance())

