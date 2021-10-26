import time
import threading

def thread1(i):
    time.sleep(3)
    #print('No. printed by Thread 1: %d' %i)

def thread2(i):
    time.sleep(3)
    #print('No. printed by Thread 2: %d' %i)
# Thread(group=None,target=None,name=None,args=(),kwargs={})
# run()
#isAlive() , join(),setname(),getname(),setDaemon(),getDaemon, 
if __name__ == '__main__':
    t1 = threading.Thread(target=thread1, args=(10,))
    t2 = threading.Thread(target=thread2, args=(12,))
    t1.start()
    t2.start()
    print("No. of active threads: " ,threading.active_count())
    t1.join()
    t2.join()