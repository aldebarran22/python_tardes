"""
Prueba con hilos en Python. Dos realizando una tarea cada uno
"""

from threading import Thread
from time import sleep
from random import randint


class Mensajes(Thread):
    def __init__(self, n):
        Thread.__init__(self, name="mensajes")
        self.n = n

    def run(self):
        for i in range(self.n):
            print(self.name, "mensaje", i)
            sleep(randint(1, 3))


class Aleatorio(Thread):
    def __init__(self, num):
        Thread.__init__(self, name="Aleatorio")
        self.num = num

    def run(self):
        for i in range(self.num):
            print(self.name, "Aleatorio: ", randint(1, 20))
            sleep(randint(0, 2))


if __name__ == "__main__":
    m = Mensajes(10)
    a = Aleatorio(8)
    m.start()
    a.start()
    print("Main termina ...")
