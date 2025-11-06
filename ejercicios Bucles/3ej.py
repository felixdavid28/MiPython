#Ejercicio 3
#Escribir un programa que pida al usuario un número entero positivo y muestre por
#pantalla todos los números impares desde 1 hasta ese número separados por comas.
e=int(input("dime un número entero positivo"))
for i in range (1,e+1,2):
    print(i, end=",")
    