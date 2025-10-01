#23. Modifica el programa anterior para establecer si la nota es un excelente (8.5 a 10), un notable (>=6.5 -<8.5), satisfactorio (<6.5 -5) o insuficiente (<5). Controla que la nota introducida esté entre 0 y 10. Utilizar elif sin operadores lógicos.

nota = float(input("Introduce la nota de tu último examen: "))

if nota <= 10:
    if nota >= 0:
        if nota < 5:
            print("Has sacado un", nota, "así que has suspendido. ")
        elif nota < 6.5:
            print("Has sacado un", nota, "así que tienes un satisfactorio. ")
        elif nota < 8.5:
            print("Has sacado un", nota, "así que tienes un notable. ")
        elif nota <= 10:
            print("Has sacado un", nota, "así que tienes un excelente. ")
    else: 
        print("Esa nota no está entre 0 y 10. ")
else:
    print("Esa nota no está entre 0 y 10. ")