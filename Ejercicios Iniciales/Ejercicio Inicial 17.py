#17. Calcula el índice de masa corporal IMC de una persona, introduciendo por teclado el peso (en kg) y dividiendo por la estatura (en metros y elevado al cuadrado). Si el resultado es igual o superior a 25, debe aparecer un mensaje informando de sobrepeso.

peso = int(input("Introduce tu peso en kg, por favor: "))
estatura = float(input("Introduce tu altura en metros, por favor: "))

IMC = peso/estatura**2

if IMC < 25:
    print("Tu IMC (Índice de Masa Corporal) es de", IMC, ", así que no tienes ningún problema. ")
elif IMC >= 25:
    print("Tu IMC (Índice de Masa Corporal) es de", IMC, ", lo que significa que tienes sobrepeso. ")