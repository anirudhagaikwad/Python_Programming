#Format date using strftime()
""""
The strftime() method is defined under classes date, 
datetime and time. The method creates a formatted string from a given date, 
datetime or time object.

"""

from datetime import datetime

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

year = now.strftime("%Y")
print("year:", year)

month = now.strftime("%m")
print("month:", month)

day = now.strftime("%d")
print("day:", day)

time = now.strftime("%H:%M:%S")
print("time:", time)

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)	

""""
Format Code:::

    %Y - year [0001,..., 2018, 2019,..., 9999]
    %m - month [01, 02, ..., 11, 12]
    %d - day [01, 02, ..., 30, 31]
    %H - hour [00, 01, ..., 22, 23
    %M - month [00, 01, ..., 58, 59]
    %S - second [00, 01, ..., 58, 59]



"""