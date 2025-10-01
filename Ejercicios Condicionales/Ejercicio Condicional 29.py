#29. Busca Internet qué función permite obtener la longitud de un String, realiza un programa que al introducir una frase devuelva la longitud

frase = str(input("Introduce una frase cualquiera: "))
longitud = 0

for i in frase:
    longitud += 1

print("La longitud de esa frase es de", longitud, "carácteres. ")