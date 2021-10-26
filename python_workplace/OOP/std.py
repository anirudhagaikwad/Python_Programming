class Stdinfo:
    section="primary"

    # def __init__(self,name,age):
    #     self.name=name
    #     self.age=age

for i in range(1,3):
    tig=input("Enter bird name:: "  )
    tigage=int(input("Enter bird age:: "  ))
    stdobj=Stdinfo()
    stdobj.name=tig
    stdobj.age=tigage
    print("\n Obj ",stdobj.name,str(stdobj.age))

print("Obj ",stdobj.name,str(stdobj.age))
print(stdobj.section)