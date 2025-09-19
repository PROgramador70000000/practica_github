#18. Cines Paradiso celebran su décimo aniversario y por ser un día especial realizan importantes descuentos. A los adultos se les aplicará un 10% de descuento y a los menores de 18 años un 50%. Si la entrada cuesta 12 euros, calcula el total a pagar introduciendo por teclado el número de menores y el número de adultos que asisten al cine.

print("Buenos días, hoy Cines Paradiso cumple diez años, y para celebrarlo regala descuentos inimaginables. Para los adultos, un 10 por ciento de descuento y a los menores de 18 años, un 50. ")
print("En este programa te falicitamos la tarea de saber el precio que tendríais que pagar tú y tu familia, teniendo en cuenta que la entrada inicial son 12 euros, y solo tendrás que decirnos cuantas personas sois. ")

mayores = int(input("Introduce el número de personas mayores de 18 años, por favor: "))
menores = int(input("Introduce el número de personas menores de 18 años, por favor: "))

precio_mayores = mayores * 10.8
precio_menores = menores * 6
total = precio_mayores + precio_menores

print("El precio de los mayores en total sería de", format(precio_mayores, ".2f"), "euros.")
print("El precio de los menores en total sería de", precio_menores, "euros. ")
print("¡Y el precio total sería de solo", total, "euros!")