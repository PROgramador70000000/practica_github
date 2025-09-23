#13. Realiza un programa que, a partir introducir el lado de un cubo, presente por pantalla el área y para calcular el volumen utiliza el operador de exponente.

lado = float(input("Introduce la longitud del lado del cubo: "))
unidad = input("Introduce la unidad de medida (por ejemplo, cm, m): ")

if unidad.isalpha():
    unidadcorrecta = True
else:
    unidadcorrecta = False

area = 6 * (lado ** 2)
volumen = lado ** 3

if unidadcorrecta:
    print("El área del cubo es:", area, unidad + "²")
    print("El volumen del cubo es:", volumen, unidad + "³")
else:
    print("La unidad de medida no es correcta. Por favor, introduce solo letras.")
