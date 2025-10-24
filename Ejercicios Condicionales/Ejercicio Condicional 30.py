#30. Realiza un programa que controle si la longitud de una frase introducida por teclado es igual, menor o mayor de 11 caracteres. Utiliza elif

frase = str(input("Introduce una frase cualquiera: "))

longitud = len(frase)

if longitud < 11:
    print("La longitud es de", longitud, " así que es menor de 11. ")
elif longitud == 11:
    print("La longitud es de", longitud, " así que es igual a 11. ")
elif longitud > 11:
    print("La longitud es de", longitud, " así que es mayor de 11. ")