class ecuacionlineal:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f
    def tieneSolucion(self):
        return (self.__a * self.__d - self.__b * self.__c) != 0
    def getX(self):
        den=self.__a * self.__d - self.__b * self.__c
        return (self.__e * self.__d - self.__b * self.__f) / den
    def getY(self):
        den=self.__a * self.__d - self.__b * self.__c
        return (self.__a * self.__f - self.__e * self.__c) / den

entrada = input("Ingrese los valores de a, b, c, d, e y f separados por espacios: ")
val=[float(num) for num in entrada.split()]
eq= ecuacionlineal(val[0], val[1], val[2], val[3], val[4], val[5])
if eq.tieneSolucion():
    print("La ecuacion tiene solucion")
    print("El valor de x es: ", eq.getX())
    print("El valor de y es: ", eq.getY())
else:
    print("La ecuacion no tiene solucion")