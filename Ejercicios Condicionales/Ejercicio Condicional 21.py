#21. Programa que calcula una ecuación de segundo grado. Controla que el valor de la raíz cuadrada no de un valor negativo

import math

a = float(input("Vamos a resolver una ecuación de segundo grado, del tipo ax2 + bx + c. Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))

raiz = (b ** 2) - (4 * a * c)

if raiz < 0:
    print("No se puede hacer la raíz de un número negativo, de modo que no se puede resolver esta ecuación. ")
else: 
    x1 = ((-1 * b) + math.sqrt(raiz)) / (2 * a)
    x2 = ((-1 * b) - math.sqrt(raiz)) / (2 * a)

    print("Las dos posible soluciones de esta ecuación son:", x1, "y", x2)

