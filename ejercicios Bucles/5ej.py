#Ejercicio 5
#Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
#y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
#año que dura la inversión.
# Ejercicio 5
# Calcular el capital obtenido cada año de una inversión
c = float(input("Dime la cantidad a invertir: "))
k = float(input("Dime el interés anual (en %): "))
a = int(input("Dime los años: "))

for i in range(1, a + 1):
    c = c * (1 + k / 100)
    print(f"Año {i}: capital = {c:.2f} €")
