#Primero asignar los dos números a variables.
num1=int(input("Introduce un número: "))
num2=int(input("Introduce otro número: "))

#Luego hacer las operaciones y asignarlas a variables.
suma=num1+num2
resta=num1-num2
multi=num1*num2
divi=num1/num2

#Por último imprimir los resultados.
print("La suma es ",suma)
print("La resta es ",resta)
print("La multiplicación es ",multi)
print("La división es ",divi)

#Tres extras:
pot=num1**num2
mod=num1%num2
divi_ent=num1//num2

print("La potencia es ",pot)
print("El módulo es ",mod)
print("La división entera es ",divi_ent)
