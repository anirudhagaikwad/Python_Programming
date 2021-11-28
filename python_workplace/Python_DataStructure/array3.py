# Python code to demonstrate the working of
# count() and extend()
#count() :- This function counts the number of occurrences of argument mentioned in array.

#extend(arr) :- This function appends a whole array mentioned in its arguments to the specified array.

# importing "array" for array operations
import array

# initializing array 1 with array values
# initializes array with signed integers
arr1 = array.array('i',[1, 2, 3, 1, 2, 5])

# initializing array 2 with array values
# initializes array with signed integers
arr2 = array.array('i',[1, 2, 3])

# using count() to count occurrences of 1 in array
print ("The occurrences of 1 in array is : ")
print (arr1.count(1))

# using extend() to add array 2 elements to array 1
arr1.extend(arr2)

print ("The modified array is : ")
for i in range (0,9):
	print (arr1[i])
