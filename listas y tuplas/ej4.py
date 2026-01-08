#Escribir un programa que pregunte al usuario los números ganadores de la lotería
#primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
#a mayor.
numeros = []
cantidad = int(input("¿Cuántos números quieres introducir? "))
for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    numeros.append(numero)
numeros.sort()
print("\nNúmeros ganadores ordenados de menor a mayor:")
print(numeros)
