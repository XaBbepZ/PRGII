import math
class estadistica:
    def __init__(self, lst):
        self.__lst = lst

    def promedio(self):
        return sum(self.__lst) / len(self.__lst)

    def desviacion(self):
        prom=self.promedio()
        return math.sqrt(sum((x - prom) ** 2 for x in self.__lst) / (len(self.__lst)-1))
entrada = input("Ingrese los valores separados por espacios: ")
val=[float(num) for num in entrada.split()]
est= estadistica(val)
print("El promedio es: ", f"{est.promedio():.2f}")
print("La desviacion estandar es: ", f"{est.desviacion():.5f}")