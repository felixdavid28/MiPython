#Escribir un programa que cree un diccionario simulando una cesta de la compra. El
#programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta
#que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la
#compra y el coste total, con el siguiente formato
# Crear un diccionario vacío para la cesta de la compra
diccionario = {}
respuesta= 0
total= 0
while respuesta !="si":
    articulo= input("¿Qué articulo quieres añadir? ")
    precio= int(input("¿Cual es el precio del articulo?  "))
    diccionario[articulo]=precio
    total = total + precio
    respuesta= input("¿Quieres terminar la cesta?")
print ("LISTA DE LA COMPRA")
for articulo, precio in diccionario.items():
    print (articulo, " = ", precio, "€")
print("TOTAL DE LA CESTA = ",total)
