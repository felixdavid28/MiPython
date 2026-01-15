#Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
#y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje
#<nombre> tiene <edad> años, vive en <dirección> y su número de
#teléfono es <teléfono>.
nombre= input("Introduzca su nombre: ")
edad= input("Introduzca su edad: ")
direccion= input("Introduzca su diereccion: ")
telefono= input("Introduzca su telefono: ")
usuario={
    "nombre" : nombre,
    "edad" : edad,
    "direccion" : direccion,
    "telefono" : telefono,
}
print  (f"{usuario['nombre']} tiene {usuario['edad']} años, vive en {usuario['direccion']} y su numero de telefono es {usuario['telefono']}")



