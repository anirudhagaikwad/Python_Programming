import threading
import time

#threading.Timer(interval,function,args=[],kwargs={})
def task():
  print("Timer object is getting executed...")

if __name__=='__main__':
  t = threading.Timer(5, task)
  print("Starting the timer object...")
  t.start() # after 5 seconds, task will be executed
  
  # cancelling the timer object before start
  print("cancelling the timer object")
  t.cancel()