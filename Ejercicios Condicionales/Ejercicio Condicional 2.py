#20. A partir del ejercicio anterior, forzar que el usuario solo pueda introducir por teclados números entre 0 y 10

num1 = float(input("Introduce el primer número. Tiene que ser un valor entre 0 y 10: "))
num2 = float(input("Introduce el segundo número. Tiene que ser un valor entre 0 y 10: "))

if (num1 >= 0 and num1 <= 10) and (num2 >= 0 and num2 <= 10): 
    if (num1 < num2):
        print("El segundo número es el más grande. ")
    elif (num1 > num2):
        print("El primer número es el más grande. ")
    else:
        print("Los dos número son iguales. ")
else: 
    print("Uno de los dos valores no está entre el rango establecido. ")

