# Python Programm to understand how to write Numeric Built-in type
""""
type() function to know which class a variable or a value belongs to
and the isinstance()function to check if an object belongs to
a particular class.
"""

x=10 # Numeric Type - integer
print('Value Store in X is : ',x)
print('x is type of : ',type(x))
print('x is instance of Integer : ',isinstance(x,int))

x=2.5 # Numeric Type - Float
print('x is instance of Float : ',isinstance(x,type(x)))

x=5+2j # Numeric Type Complex
print('x is instance of Complex : ',isinstance(x,type(x)))

