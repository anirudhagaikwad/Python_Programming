#Program to Rise Exception
class TestAge:
		def agetest(self):
				try:  
					age = int(input("Enter the age : "))  
					if age<18:  
						raise ValueError;  
					else:  
						print("the age is valid for Vote")  
				except ValueError: 
						print("the age is not Eligible for Vote")
				return 

obj=TestAge()
obj.agetest()
				
				
         
