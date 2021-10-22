
#Current time using time module
import time

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)
print(current_time)


#Sleep Function
print("This is printed immediately.")
time.sleep(3.4)
print("This is printed after 3.4 seconds.")