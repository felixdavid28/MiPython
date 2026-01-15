# Diccionario con frutas y precios por kilo
frutas = {
    "platano": 1.35,
    "manzana": 0.80,
    "pera": 0.85,
    "naranja": 0.70
}

dime = input("Dime la fruta: ")
kilos = float(input("Dime el número de kilos: "))

if dime in frutas:
    precio = frutas[dime]
    total = kilos * precio
    print(f"El precio de {kilos} kilos de {dime} es {total:.2f} €")
else:
    print("Lo siento, esa fruta no está en el diccionario.")
