
# A simple generator function
""""
	yield statement pauses the function saving all 
	its states and later continues from there on successive calls.
	"""
def my_gen():
    n = 1
    print('This is printed first')
    # Generator function contains yield statements
    yield n #yield use for return some value from functions

    n += 1
    print('This is printed second')
    yield n
	
    n += 1
    print('This is printed at last')
    yield n
""""
to see output:::
x=my_gen()
next(a)

"""	
	
""""
Differences between Generator function and a Normal function::::
    Generator function contains one or more yield statement.
    When called, it returns an object (iterator) but does not start execution immediately.
    Methods like __iter__() and __next__() are implemented automatically. So we can iterate through the items using next().
    Once the function yields, the function is paused and the control is transferred to the caller.
    Local variables and their states are remembered between successive calls.
    Finally, when the function terminates, StopIteration is raised automatically on further calls.


"""	