#25. Repite el programa número 23 pero en esta ocasión utilizando operadores lógicos.

nota = float(input("Introduce la nota de tu último examen: "))

if (nota >= 0 and nota <= 10):
    if nota < 5:
        print("Has sacado", nota, "así que estás suspendido. ")
    elif nota < 6.5 and nota >= 5:
        print("Has sacado", nota, "así que tienes un satisfactorio. ")
    elif nota < 8.5 and nota >=6.5:
        print("Has sacado", nota, "así que tienes un notable.")
    elif nota <= 10 and nota >= 8.5:
        print("¡Felicidades! Tienes un", nota, "así que tienes un excelente. ")
else:
    print("Esa nota no está entre 0 y 10... ¿No es un poco raro?")
