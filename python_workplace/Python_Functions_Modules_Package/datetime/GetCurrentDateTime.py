#Get Current Date and Time
import datetime 


""""
One of the classes defined in the datetime module is datetime class.
We then used now() method to create a 
datetime object containing the current local date and time.
"""
datetime_object = datetime.datetime.now()
print(datetime_object)


#Get Current Date
date_object = datetime.date.today()
print(date_object)

""""
instantiate date objects from the date class.
A date object represents a date (year, month and day).
"""
#Date object to represent a date
d = datetime.date(2019, 5, 31)
print(d)

#Print today's year, month and day
today = datetime.date.today() 

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)

#Time object to represent time
# time(hour = 0, minute = 0, second = 0)
print ("\n Time")
a = datetime.time()
print("a =", a)

# time(hour, minute, second, microsecond)
d = datetime.time(11, 34, 56, 234566)
print("d =", d)



