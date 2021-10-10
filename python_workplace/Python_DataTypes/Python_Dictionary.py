
""""
dictionaries are defined within braces {} 
with each item being a pair in the form key:value. 
Key and value can be of any type.
"""
#keys must be of immutable type and must be unique.

d = {1:'value_of_key_1','key_2':2} #Dictionary
print('d is instance of Dictionary : ',isinstance(d,type(d)))

#To access values, dictionary uses keys.
print("using key access value d[1] = ", d[1])
print("using key access value d['key_2'] = ", d['key_2'])

print('access values using get() : ',d.get(1))#access values using get()


# update value
d[1] = 'Banana'

print('update d[1] = Banana : ',d[1])


# add item
d['Dry Fruit'] = 'Badam'

print('add item d[Dry Fruit] = Badam',d)


print('d.items() :',d.items()) #To access the key value pair, you would use the .items() method

print('d.keys() :',d.keys()) #To access keys separately use keys() methos

print('d.values() :',d.values()) #To access values separately use values() methos

#print("d[2] = ", d[2]); # Generates error


# remove dict pair
d.pop(1) #remove a particular item, returns its value
print('after d.pop(1) : ',d)

d.popitem() #remove an arbitrary item,return (key,value)
print('after d.popitem() : ',d) 

# remove all items
d.clear()
print('after use function clear() : ',d)

# delete the dictionary itself
del d
#print('after delete dictionary : ',d)