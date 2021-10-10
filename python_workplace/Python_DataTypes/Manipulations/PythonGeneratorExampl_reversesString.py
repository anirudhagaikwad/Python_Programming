
#example of a generator that reverses a string.
def rev_str(my_str):
    length = len(my_str)
    for i in range(length - 1,-1,-1):
        yield my_str[i]

# For loop to reverse the string
# Output:
# o
# l
# l
# e
# h
for char in rev_str("hello"):
     print(char)
	 
""""
range() function to get the index in reverse order using the for loop.
"""	 