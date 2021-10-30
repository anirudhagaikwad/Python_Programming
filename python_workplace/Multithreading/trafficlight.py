# Python multi-threaded event to achieve traffic light case
import time,threading
#Open event
event = threading.Event()
count = 0
class Lighter(threading.Thread):
    def run(self):
        while True:
            global count
            count += 1
            time.sleep(0.4)
            event.set()
                         #Set the green light time to 10s and the red light to 10s
            if count>10 and count<=20:
                event.clear()
                print('\033[41;1m red light ..\033[0m')
            elif count > 20:
                count = 0
                event.set()
                print('\033[42;1m green light ..\033[0m')
            else:
                print('\033[42;1m green light ..\033[0m')
 
 
class Car(threading.Thread):
    def __init__(self,name):
        super(Car,self).__init__()
        self.name = name
    def run(self):
        time.sleep(0.5)
        if event.is_set():
            print('{} passed the light'.format(self.name))
        else:
            print('{} is waiting the green light'.format(self.name))
 
l = Lighter()
l.start()
 #Start 50 cars and let them pass the traffic lights
for i in range(50):
    time.sleep(1)
    c = Car('car{}'.format(i))
    c.start()