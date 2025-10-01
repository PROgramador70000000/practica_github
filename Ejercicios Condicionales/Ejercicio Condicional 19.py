#19. Programa que introduzca dos números y devuelva cuál de los dos es mayor, menor o son iguales

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if num1 < num2:
    print("El segundo número es el más grande. ")
elif num1 > num2:
    print("El primer número es el más grande. ")
else:
    print("Los dos número son iguales. ")