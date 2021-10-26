import threading
import time

def task(event, timeout):
  print("Started thread but waiting for event...")
  # make the thread wait for event with timeout set
  event_set = event.wait(timeout)
  if event_set:
    print("Event received, releasing thread...")
  else:
    print("Time out, moving ahead without event...")
    
if __name__ == '__main__':
  # initializing the event object
  e = threading.Event()
  
  # starting the thread
  thread1 = threading.Thread(name='Event-Blocking-Thread', target=task, args=(e,4))
  thread1.start()
  # sleeping the main thread for 3 seconds
  time.sleep(3)
  # generating the event
  e.set()
  print("Event is set.")