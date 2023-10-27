import threading, random, time

class Producer(threading.Thread):  

    def __init__(self, integers, sem_huecos, sem_items, mutex):       
        threading.Thread.__init__(self)
        self.integers = integers
        self.sem_huecos = sem_huecos
        self.sem_items = sem_items
        self.mutex = mutex
    
    def run(self):      
        while True:
            integer = random.randint(0, 256)
            print ('PRODUCTOS produce: %d - %s' % (integer, self.name))
            self.sem_huecos.acquire()
            
            self.mutex.acquire()
            self.integers.append(integer)            
            self.mutex.release()

            self.sem_items.release()
            time.sleep(1)


###############################################################################
            
class Consumer(threading.Thread):
   
    def __init__(self, integers, sem_huecos, sem_items, mutex):
      
        threading.Thread.__init__(self)
        self.integers = integers
        self.sem_huecos = sem_huecos
        self.sem_items = sem_items
        self.mutex = mutex
    
    def run(self):
        
        while True:
            self.sem_items.acquire()
            
            self.mutex.acquire()
            integer = self.integers.pop()
            print ('CONSUMIDOR consume: %d - %s' % (integer, self.name))          
            self.mutex.release()

            self.sem_huecos.release()
            time.sleep(3)

#################################################################################


def main():
    integers = []
    sem_huecos = threading.Semaphore(10)
    sem_items = threading.Semaphore(0)
    mutex = threading.Lock()
    t1 = Producer(integers, sem_huecos, sem_items, mutex)
    t2 = Consumer(integers, sem_huecos, sem_items, mutex)
    t1.start()
    t2.start()
    t1.join()
    t2.join()

if __name__ == '__main__':
    main()
