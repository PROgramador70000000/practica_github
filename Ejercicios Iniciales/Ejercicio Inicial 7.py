#7. programa que calcule dos operandos con los 7 operadores vistos en clase. ¿Cómo puedes forzar que el resultado de la división tenga 2 decimales?

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division_entera = num1 // num2
division = num1 / num2
division_entera = num1 // num2
modulo = num1 % num2
potencia = num1 ** num2

print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", multiplicacion)
print("La división es:", format(division, ".2f"))
print("La división entera es:", division_entera)
print("El módulo es:", modulo)
print("La potencia es:", potencia)