# import module sys to get the type of exception
"""" sys module provides access to some variables used or maintained by the interpreter 
and to functions that interact strongly with the interpreter. 
It is always available."""
import sys

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",entry,"is",r)
""""
sys.exc_info()
This function returns a tuple of three values that give information about
the exception that is currently being handled.
		
"""
