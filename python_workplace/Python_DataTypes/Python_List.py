# Python Programm to understand how to write List Data type
# Lists are mutable(that means you can change state/value)
# List Index starts form 0 in Python.

""""
All the items in a list do not need to be of the same type
list is created by placing all the items (elements) inside a square bracket [ ], 
separated by commas.
"""

x=['python',2020,2019,'django',2018,20.06,40j] #List

# you can show list using diffrent way
print('List x : ',x[:]) # we can use the index with slice operator [] to access an item in a list. Index starts from 0.
print('List x : ',x[:])
print('List x : ',x[0:])
print('List x : ',x)

# extract/access specific element from list
print('List x[0] : ',x[0])
print('List x[1:5] : ',x[1:5]) # characters from position(index) 1 (included) to position(index) 5 (excluded i.e. 5-1) it will print index 1 element to index 4 element

""""
Python allows negative indexing for its sequences.The index of -1 refers to the last item,
-2 to the second last item and so on.
"""
print('List negative indexing x[-2]: ',x[-2])
print('List negative indexing x[0:-4]: ',x[0:-4])
print('List negative indexing x[:-4]: ',x[:-4])

# Add Values in List
x.append(25) # add one item to a list using append() method
print('After add 25 Value in List : ',x)

x.insert(2,'hello') # insert one item at a desired location by using the method insert()
print('After inser hello in List on second index : ',x)

x.extend([0,1,2,3]) # add several items using extend() method.
print('After extend list with [0,1,2,3] : ',x[:])


# change the index value/item
x[5]=2017
print('After change index 5 value : ',x)

x[6:8]=['q','w','r']
print('After change x[6:8]= q,w,r : ',x)


# delete items from list
del x[5] # delete one or more items from a list using the keyword del.
print('List after delete x[5] : ',x)

x.pop(6) # pop() method to remove an item at the given index.
print('List after pop x[6] : ',x)

x.remove(3) # remove() method to remove the given item
print('List after remove 40j : ',x)

x.clear()
print('After clear List : ',x)






