try:
    c=open("te.txt",'r+') 
    c.write("Hello Python using Django framework")
    print(c.read())
    c.write("####Hello Python using Django framework####")
    c.write("&&&&Hello Python using Django framework&&&&")

except:
      print("file close successfully")

finally:    
    c.close()