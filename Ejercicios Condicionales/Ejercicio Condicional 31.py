#31. Asigna a una variable de texto la siguiente frase: A quién madruga Dios ayuda. Comprueba si existen las siguientes palabras mostrando por pantalla la posición de su índice.

frase = str("A quién madruga Dios ayuda. ")
palabra = str(input("Introduce una palabra que se encuentre en la frase A quién madruga Dios le ayuda: "))
palabra_en_frase = frase.find(palabra)

if palabra_en_frase == -1:
    print("La palabra no se encuentra en esa frase. ")
else:
    print("La palabra empieza en la posición", (palabra_en_frase + 1), "de la frase. ")