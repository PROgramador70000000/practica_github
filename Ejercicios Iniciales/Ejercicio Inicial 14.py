#14. Realiza un programa que a partir de introducir el diámetro de un círculo calcule el área y perímetro. Importa la librería math y utiliza el valor PI para hacer el cálculo. Redondea el resultado a un decimal.
import math

diametro = float(input("Introduce el diámetro del círculo: "))
unidad = input("Introduce la unidad de medida (por ejemplo, cm, m): ")

if unidad.isalpha():
    unidadcorrecta = True
else:
    unidadcorrecta = False

radio = diametro / 2 
area = math.pi * radio**2
perimetro = math.pi * diametro

if unidadcorrecta:
    print("El área del círculo es: ", format(area,".2f"), unidad +"²")
    print("El perímetro del círculo es: ", format(perimetro, ".2f"), unidad)
else:
    print("Unidad de medida no válida.")