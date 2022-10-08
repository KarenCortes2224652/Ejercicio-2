# Ejercicio 2:
print("-----------------------------------")
print("--- CALCULAR - NÚMERO - INVERSO ---")
print("-----------------------------------")

#Input
num = int(input("Ingresa un número entero y positivo: "))
m = num
i = 0

#Processing
while num > 0:
    u = num % 10
    i = i * 10 + u
    num = num // 10
print("El número que acabas de ingresar es:",m)
print("El número inverso de este es :",i)

