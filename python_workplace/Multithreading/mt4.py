import threading
import time

class MyThread(threading.Thread):
  # overriding constructor
  def __init__(self, i):
    # calling parent class constructor
    threading.Thread.__init__(self)
    self.x = i
    
  # define your own run method
  def run(self):
    print("Value stored is: ", self.x)
    time.sleep(3)
    print("Exiting thread with value: ", self.x)
    

thread1 = MyThread(1)
thread1.start()
thread2 = MyThread(2)
thread2.start()