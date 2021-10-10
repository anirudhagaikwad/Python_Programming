""""
Using for loop we can iterate through a string. 
Here is an example to count the number of 'l' in a string.
"""
count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')