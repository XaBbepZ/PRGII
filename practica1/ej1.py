import time
import random 
class cronometro:
    def __init__(self):
        self.__inicia=time.time()
        self.__finaliza=self.__inicia
    def get_inicia(self):
        return self.__inicia
    def get_finaliza(self):
        return self.__finaliza
    def inicia(self):
        self.__inicia=time.time()
    def detener(self):
        self.__finaliza=time.time()
    def lapsoDeTiempo(self):
        return int((self.__finaliza-self.__inicia)*1000)

def ordenar (lista):
    for i in range(len(lista)):
        min=i
        for j in range(i+1,len(lista)):
            if lista[j]<lista[min]:
                min=j
        lista[i],lista[min]=lista[min],lista[i]
    return lista

N=100000
print("Se generara una lista de ",N," elementos aleatorios")
lista=[random.randint(1, 100000) for _ in range(N)]
c=cronometro()
c.inicia()
print("ordenando la lista...")
ordenar(lista)
c.detener()
print("ordenado con exito")
print("Tiempo de ejecucion: ",c.lapsoDeTiempo()," milisegundos")