
from collections import Counter
from threading import Thread
from random import randint

class Factorizar(Thread):

    def __init__(self, numero):
        Thread.__init__(self)
        self.numero = numero
        self.primos = []
        self.factores = None

    def run(self):       
        n = self.numero

        for i in range(2, n + 1):
            while n % i == 0:
                self.primos.append(i)
                n = n / i

        self.factores = dict(Counter(self.primos))

if __name__=='__main__':
    L = [randint(10,200) for _ in range(6)]
    print(L)

    hilos = []
    for numero in L:
        hilo = Factorizar(numero)
        hilos.append(hilo)
        hilo.start()

    for hilo in hilos:
        hilo.join()
    
    # Ya han terminado todos los hilos:
    for h in hilos:
        print(h.numero, h.factores)

    
