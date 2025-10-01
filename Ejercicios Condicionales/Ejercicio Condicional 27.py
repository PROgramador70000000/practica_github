#27. Mejora el programa anterior para controlar que el valor introducido es una letra y en caso de introducir un número, aparezca un aviso por pantalla

letra = str(input("Introduce una letra: "))

if (letra.isalpha()):
    if (letra.isupper()):
        print("La letra está en mayúscula. ")
    elif (letra.islower()):
        print("La letra es minúscula. ")
elif (letra.isdigit()):
    print("Eso no es una letra, eso es un número. ")