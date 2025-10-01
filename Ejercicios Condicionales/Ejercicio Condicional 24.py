#24. Corrige los errores del siguiente código y comprueba que se ejecuta correctamente

#El primer error es que una variable no puede empezar por número, así que cambié 1var por var1.
# Yo recomendaría poner a cada variable el nombre de lo que asigna, para tenerlo claro y evitar errores posteriores. 
var1 = float(input("Introduce tu peso en kilos: "))
var2 = float(input("Introduce tu altura en metros: "))

#Para asignar un valor a una variable, se utiliza solo un igual (=). Los dos iguales son una comparación. 
var_imc = var1 / var2 ** 2

#Las llaves en print solo se pueden usar si quieres cambiar el formato de print, de manera que tendríamos que poner una "f" antes de las comillas. 
#De esta manera: print(f"Si pesas {var1} kilos y mides {var2} metros, tu IMC es de {var_imc}. ")
#La otra manera es usar las comas:
print("Si pesas", var1, "kilos y mides", var2, "metros, tu IMC es de", var_imc)

#Nos ha faltado poner los dos puntos desspués del condicional en if. 
if var_imc > 25:
    print("Hay sobrepeso. ")
else: 
    print("Estás dentro de los parámetros normales. ")