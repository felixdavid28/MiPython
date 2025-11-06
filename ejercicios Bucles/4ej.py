#Ejercicio 4
#Escribir un programa que pida al usuario un número entero positivo y muestre por
#pantalla la cuenta atrás desde ese número hasta cero separados por comas.
n=int(input("dime un número entero positivo"))
for i in range (n,0-1,(-1)):
    print(i, end=",")