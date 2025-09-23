#10. Introduce por teclado dos números y muestre por pantalla la siguiente información: cociente, resto y si el dividendo es par o impar.

dividendo = int(input("Introduce el dividendo: "))
divisor = int(input("Introduce el divisor: "))

division = dividendo // divisor
resto = dividendo % divisor

if dividendo % 2 == 0:
    par_impar = "par"
else:
    par_impar = "impar"

print("Cociente:", division)
print("Resto:", resto)
print("El dividendo es:", par_impar)