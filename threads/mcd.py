from threading import Thread
from time import sleep
from random import randint
from collections import Counter

N = 12


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
                print(self.name, "factor:", i)
                self.primos.append(i)
                n = n / i
        self.factores = dict(Counter(self.primos))


if __name__ == "__main__":
    L = [randint(100, 500) for _ in range(N)]
    print(L)

    hilos = []
    for i in L:
        hilo = Factorizar(i)
        hilos.append(hilo)
        hilo.start()

    # Esperar a que terminen
    for h in hilos:
        h.join()

    # Ya han terminado, imprimir resultado
    for h in hilos:
        print(h.numero, h.factores)
