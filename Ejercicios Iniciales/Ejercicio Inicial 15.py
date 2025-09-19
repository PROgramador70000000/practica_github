#15. Utiliza el valor Pi de la librería math para calcular el área y volumen de un cilindro, introduciendo por teclado el valor de radio y altura. Resultado con 2 decimales.
import math

radio = float(input("Introduce el valor del radio del cilindro: "))
altura = float(input("Introduce el valor de la altura del cilindro: "))
unidad = input("Introduce la unidad de medida (por ejemplo, cm, m): ")

if unidad.isalpha():
    unidadcorrecta = True
else:
    unidadcorrecta = False

if unidadcorrecta:
    area = 2 * math.pi * radio * (radio + altura)
    volumen = math.pi * radio**2 * altura
    print("El área del cilindro es: ", format(area, ".2f"), unidad + "²")
    print("El volumen del cilindro es: ", format(volumen, ".2f"), unidad + "³")
else:
    print("Unidad de medida no válida.")
