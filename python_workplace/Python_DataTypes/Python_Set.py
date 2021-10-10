#Set is an unordered collection of unique items
#Sets are mutable.
""""
set are unordered collection, 
indexing has no meaning. 
Hence the slicing operator [] does not work.

"""

x={'python',2020,2019,'django',2018,20.06,40j} #Set

print('Set x : ',x)

print('x is instance of Set : ',isinstance(x,type(x)))


""""
We can add single element using the add() method 
and multiple elements using the update() method. 
The update() method can take tuples,
 lists, strings or other sets as its argument.
"""
x.add(2) # add an element
print('Set x after add 2 : ',x)

x.update([5,9,8,7]) # add multiple elements
print('Set x after update([5,9,8,7]) : ',x)


""""
particular item can be removed from set using methods, discard() and 
remove().The only difference between the two is that, while using discard
()if the item does not exist in the set, it remains unchanged. 
But remove() will raise an error in such condition.
"""

x.discard(2019)
print('Set x after discard(2019)',x)

x.remove(5)
print('Set x after remove(5)',x)