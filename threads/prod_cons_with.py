from threading import *

import time, random


class Productor(Thread):
	
	def __init__(self,mutex,sem_huecos,sem_items, buff):
		Thread.__init__(self)
		self.__mutex = mutex
		self.__sem_huecos = sem_huecos
		self.__sem_items = sem_items
		self.__buff = buff
	
	def run(self):
		while True:
			# Generar item:
			numero = random.randint(1,100)
			
			# Esperar a que tenga huecos
			self.__sem_huecos.acquire()
			
			# Hace acquire y release:
			with self.__mutex:
			
				# Colocar el numero en la lista:
				self.__buff += [numero]
				print ("P coloca el:",numero)
				print (self.__buff)
			
			# Incrementa sem de items:
			self.__sem_items.release()
			
			time.sleep(1)
			
		

class Consumidor(Thread):
	
	def __init__(self,mutex,sem_huecos,sem_items, buff, num):
		Thread.__init__(self)
		self.__mutex = mutex
		self.__sem_huecos = sem_huecos
		self.__sem_items = sem_items
		self.__buff = buff
		self.__num = num
	
	def run(self):
		
		while True:
			#Esperar por un item
			self.__sem_items.acquire()
			
			# Acceder a la lista en exclusion mutua:
			# Solo puede acceder uno simultaneamente:
			
			# Hace acquire y release:
			with self.__mutex:
		
				# Extraer un numero del buffer:
				numero = self.__buff[0]
				del(self.__buff[0])
				print ("C",self.__num,"extrae el:",numero)
				print (self.__buff)
						
			
			# indicar que hay un hueco mas:
			self.__sem_huecos.release()		
			
			time.sleep(5)
		

#Definir mutex y semaforos:
mutex = Lock()

# Inicialmente el buffer esta vacio
sem_huecos = Semaphore(10)

# No hemos generado ningun item
sem_items = Semaphore(0)

buff = []

# Crear los hilos:
prod = Productor(mutex,sem_huecos,sem_items, buff)
cons = Consumidor(mutex,sem_huecos,sem_items, buff, 1)
cons2 = Consumidor(mutex,sem_huecos,sem_items, buff, 2)

# Ponerlos en marcha:
prod.start()
cons.start()
cons2.start()

# El hilo principal espera a que terminen los hilos.
prod.join()
cons.join()
cons2.join()
