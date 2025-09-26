#22. Programa que al introducir una nota por teclado te diga si has aprobado o suspendido. Si la nota es menos de un 5 es suspenso y si la nota es 5 o mayor estás aprobado.

nota = float(input("Introduce la nota de tu último examen: "))

if (nota >= 0 and nota <= 10):
    if nota >= 5:
        print("¡Estás aprobado, felicidades! Tu nota es de", nota)
    elif nota < 5:
        print("Has sacado", nota, "así que estás suspendido. ")
else:
    print("Esa nota no está entre 0 y 10... ¿No es un poco raro?")
