
#way of automatically iterating is by using the for loop.

my_list = [4, 7, 0, 3]
for element in my_list:
						print(element)
""""
for element in iterable:
"""		
###How for loop actually works?
""""
# create an iterator object from that iterable
iter_obj = iter(iterable)

# infinite loop
while True:
    try:
        # get the next item
        element = next(iter_obj)
        # do something with element
    except StopIteration:
        # if StopIteration is raised, break from loop
        break

"""	

""""
the for loop creates an iterator object, iter_obj by calling iter() on the iterable.
Ironically, this for loop is actually an infinite while loop.

 this for loop is actually an infinite while loop.

Inside the loop, it calls next() to get the next element and executes the body of the for loop with this value. After all the items exhaust, StopIteration is raised which is internally caught and the loop ends.
Note that any other kind of exception will pass through.
"""			