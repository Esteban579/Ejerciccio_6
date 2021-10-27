# Ejercicio 6

import statistics

n1 = int(input("Introduzca el primer dato numerico: "))
n2 = int(input("Introduzca el segundo dato numerico: "))
n3 = int(input("Introduzca el tercer dato numerico: "))

n = {n1, n2, n3}

media = statistics.mean(n)
mediana = statistics.median(n)
varianza = statistics.variance(n)

print("Media: ", media)
print("Mdeiana: ", mediana)
print("Varianza: ", varianza)