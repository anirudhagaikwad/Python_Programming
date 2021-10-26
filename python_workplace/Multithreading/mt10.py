import threading
import time


#threading.Barrier(parties,action=None,timeout=None)
def start_server():
  # starting server
  print("starting the server...")
  # do some startup work
  time.sleep(2)
  

def server(b):
    start_server()
    b.wait()
    print("Server is ready.")

def client(b):
    print("waiting for server getting ready...")
    b.wait()
    print("sending request to server...")

if __name__=='__main__':
  
  b = threading.Barrier(2, timeout=5)
  # server thread
  s = threading.Thread(target=server, args=(b,))
  s.start()
  # client thread
  c = threading.Thread(target=client, args=(b,))
  c.start()

  s.join()
  c.join()
  print("Done")