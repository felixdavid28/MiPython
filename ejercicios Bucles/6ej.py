#Ejercicio 6
#Escribir un programa que pida al usuario un número entero y muestre por pantalla
#un triángulo rectángulo como el de más abajo, de altura el número introducido.
n = int(input("Dime número: "))
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print("")