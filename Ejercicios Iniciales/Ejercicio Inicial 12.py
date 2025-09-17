#12. Realiza un programa que, introduciendo en los valores de lado, base menor, base mayor y altura de un trapecio isósceles, nos devuelva por pantalla en el área y el perímetro.

lado = float(input("Introduce la longitud del lado del trapecio: "))
base_menor = float(input("Introduce la longitud de la base menor del trapecio: "))
base_mayor = float(input("Introduce la longitud de la base mayor del trapecio: "))
altura = float(input("Introduce la altura del trapecio: "))
unidad = input("Introduce la unidad de medida (por ejemplo, cm, m): ")

if unidad.isalpha():
    unidadcorrecta = True
else:
    unidadcorrecta = False

area = ((base_menor + base_mayor) * altura) / 2
perimetro = 2 * lado + base_menor + base_mayor

if unidadcorrecta:
    print("El área del trapecio es:", area, unidad + "²")
    print("El perímetro del trapecio es:", perimetro, unidad)
else:
    print("La unidad de medida no es correcta. Por favor, introduce solo letras.")
