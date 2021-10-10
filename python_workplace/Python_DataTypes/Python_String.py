#String is sequence of Unicode characters.
#its immutable
#Index starts form 0 in Python.


x='Hello world!'

# you can show element of String using diffrent way
print('String x[6] : ',x[6]) # we can use the index with slice operator [] to access an item in a String. Index starts from 0.
print('String x[:] : ',x[:])
print('String x[0:6] : ',x[0:6]) # characters from position(index) 0 (included) to position(index) 6 (excluded i.e. 5-1) it will print index 0 element to index 5 element
print('String x[:5] : ',x[:5])
print('String x : ',x)


print('len(x) = ', len(x))

print ('lower case x.lower() :',x.lower())

print ('upper case x.upper() :',x.upper())


print ('reverse String x[::-1] :',x[::-1])

default_order = "{}, {} and {}".format('hi','hello','how are you')
print('\n--- Default Order ---')
print(default_order)



