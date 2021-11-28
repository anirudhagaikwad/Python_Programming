# Python code to demonstrate the working of
# typecode, itemsize, buffer_info()

# importing "array" for array operations
import array
# from array import *

# initializing array with array values
# initializes array with signed integers
arr= array.array('i',[1, 2, 3, 1, 2, 5])

# typecode :- This function returns the data type by which array is initialised.
# itemsize :- This function returns size in bytes of a single array element.
# buffer_info() :- Returns a tuple representing the address in which array is stored and number of elements in it.

# using typecode to print datatype of array
print ("The datatype of array is : ")
print (arr.typecode)

# using itemsize to print itemsize of array
print ("The itemsize of array is : ")
print (arr.itemsize)

# using buffer_info() to print buffer info. of array
print ("The buffer info. of array is : ")
print (arr.buffer_info())
