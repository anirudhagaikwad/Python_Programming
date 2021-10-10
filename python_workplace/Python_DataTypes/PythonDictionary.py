#Program to illustrate Python Dictionary
""""
Creating a dictionary is as simple as placing items inside curly braces {}
separated by comma.An item has a key and the 
corresponding value expressed as a pair, key: value.
"""
#keys must be of immutable type and must be unique.
my_dict = {1: 'apple', 2: 'ball',3:'mango',4:'Watermelon'}

#To access values, dictionary uses keys.
print(my_dict[1])
print(my_dict.get(1))#access values using get()

# update value
my_dict[1] = 'Banana'
print(my_dict)

# add item
my_dict['Dry Fruit'] = 'Badam'
print("\n Add Item :",my_dict)

# remove a particular item
""""pop(). This method removes as item with 
the provided key and returns the value """
print("\n Remove Particular Item :",my_dict.pop('Dry Fruit'))
print(my_dict)

"""" popitem() can be used to remove 
and return an arbitrary item (key, value) form the dictionary. """
print(my_dict.popitem())
print("After PopItem:",my_dict)

""""del keyword to remove individual items 
or the entire dictionary itself."""

del my_dict[1]
print(my_dict)

my_dict.clear()
print(my_dict)

del my_dict
#print(my_dict)

