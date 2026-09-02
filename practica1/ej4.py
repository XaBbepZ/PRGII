import math
def promedio(lst):
    return sum(lst) / len(lst)
def desviacion(lst):
    prom=promedio(lst)
    return math.sqrt(sum((x - prom) ** 2 for x in lst) / (len(lst)-1))
entrada = input("Ingrese los valores separados por espacios: ")
val=[float(num) for num in entrada.split()]
print("El promedio es: ", f"{promedio(val):.2f}")
print("La desviacion estandar es: ", f"{desviacion(val):.5f}")
