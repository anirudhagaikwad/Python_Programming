#Format date using strptime()

""""
The strptime() method creates 
a datetime object from a given string (representing date and time).

The strptime() class method takes two arguments:

    string (that be converted to datetime)
    format code

"""
from datetime import datetime

date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)

""""
%d, %B and %Y format codes 
are used for day, month(full name) and year respectively.

"""