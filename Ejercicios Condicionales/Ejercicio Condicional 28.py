#28. Mejora el programa anterior para controlar también la introducción de símbolos. Utiliza elif.

letra = str(input("Introduce una letra: "))

if (letra.isalpha()):
    if (letra.isupper()):
        print("La letra está en mayúscula. ")
    elif (letra.islower()):
        print("La letra es minúscula. ")
elif (letra.isdigit()):
    print("Eso no es una letra, eso es un número. ")
else:
    print("Eso no es una letra, eso es un carácter especial. ")