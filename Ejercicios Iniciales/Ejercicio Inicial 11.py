#11. Realiza un programa que introduciendo el valor del lado de un cuadrado nos devuelva por pantalla en el área y el perímetro

lado = float(input("Introduce la longitud del lado del cuadrado: "))
unidad = input("Introduce la unidad de medida (por ejemplo, cm, m): ")

if unidad.isalpha():
    unidadcorrecta = True
else:
    unidadcorrecta = False

area = lado ** 2
perimetro = 4 * lado

if unidadcorrecta:
    print("El área del cuadrado es:", area, unidad + "²")
    print("El perímetro del cuadrado es:", perimetro, unidad)
else:
    print("La unidad de medida no es correcta. Por favor, introduce solo letras.")