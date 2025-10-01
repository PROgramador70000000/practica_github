#32. Cómo solucionarías con ayuda de métodos String el problema del ejercicio anterior para no distinguir entre mayúsculas y minúsculas

frase = str("A quién madruga Dios ayuda. ")
palabra = str(input("Introduce una palabra que se encuentre en la frase A quién madruga Dios le ayuda: "))
palabra_en_frase = frase.find(palabra)

if palabra_en_frase == -1:
    print("La palabra no se encuentra en esa frase. ")
else:
    print("La palabra empieza en la posición", (palabra_en_frase + 1), "de la frase. ")