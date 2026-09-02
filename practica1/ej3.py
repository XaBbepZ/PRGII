import math
class ecuacionc:
    def __init__(self, a, b, c):
        self.__a = a
        self.__b = b
        self.__c = c

    def getDiscriminante(self):
        return self.__b ** 2 - 4 * self.__a * self.__c

    def getRaiz1(self):
        disc=self.getDiscriminante()
        if disc < 0:
            return 0
        return (-self.__b + math.sqrt(disc)) / (2 * self.__a)
    def getRaiz2(self):
        disc=self.getDiscriminante()
        if disc < 0:
            return 0
        return (-self.__b - math.sqrt(disc)) / (2 * self.__a)

entrada= input("Ingrese los valores de a, b y c separados por espacios: ")
val=[float(num) for num in entrada.split()]
eq= ecuacionc(val[0], val[1], val[2])
disc=eq.getDiscriminante()
if disc < 0:
    print("La ecuacion no tiene solucion")
elif disc == 0:
    print("La ecuacion tiene una solucion")
    print("El valor de la raiz es: ", eq.getRaiz1())
else:
    print("La ecuacion tiene dos soluciones")
    print("El valor de la primera raiz es: ", eq.getRaiz1())
    print("El valor de la segunda raiz es: ", eq.getRaiz2())