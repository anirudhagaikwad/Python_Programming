#Nested For Loop ,Program to Print Star
n = int(input("Enter the number of rows you want to print:"))  
i,j=0,0  
for i in range(0,n):  
    print()  
    for j in range(0,i+1):  
        print("*",end="") 
