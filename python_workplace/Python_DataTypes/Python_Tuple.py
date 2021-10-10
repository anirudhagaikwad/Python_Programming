#tuples are immutable.
#defined within parentheses () where items are separated by commas
#Tuple Index starts form 0 in Python.

x=('python',2020,2019,'django',2018,20.06,40j,'python') #Tuple

# you can show tuple using diffrent way
print('Tuple x : ',x[:]) # we can use the index with slice operator [] to access an item in a tuple. Index starts from 0.
print('Tuple x : ',x[:])
print('Tuple x : ',x[0:])
print('Tuple x : ',x)

# extract/access specific element from tuple
print('Tuple x[0] : ',x[0])
print('Tuple x[1:5] : ',x[1:5]) # characters from position(index) 1 (included) to position(index) 5 (excluded i.e. 5-1) it will print index 1 element to index 4 element

""""
Python allows negative indexing for its sequences.The index of -1 refers to the last item,
-2 to the second last item and so on.
"""
print('Tuple negative indexing x[-2]: ',x[-2])
print('Tuple negative indexing x[0:-4]: ',x[0:-4])
print('Tuple negative indexing x[:-4]: ',x[:-4])


z =x.count('python') # Returns the number of items x 
print(z,'number of python string found in tuple')


z=x.index(2019) # Returns the index of the item 

print('index number of 2019 is : ',z)
