#Escribir un programa que cree un diccionario vacío y lo vaya llenado con
#información sobre una persona (por ejemplo nombre, edad, sexo, teléfono, correo
#electrónico, etc.) que se le pida al usuario. Cada vez que se añada un nuevo dato
#debe imprimirse el contenido del diccionario.

usuario = {}
usuario["nombre"] = input("Dime su nombre: ")
print(usuario)
usuario["edad"] = input("Dime su edad: ")
print(usuario)
usuario["sexo"] = input("Dime su sexo: ")
print(usuario)
usuario["telefono"] = input("Dime su teléfono: ")
print(usuario)
usuario["correo"] = input("Dime su correo electrónico: ")
print(usuario)

#otra forma
p=1
while p !=0:
    print("1.Añadir dato")
    print("0.Salir")
    p = int(input("Elige una opción: "))
    if p == 1:
        dato= input("Añade un dato: ")
        valor= input("Añade valor a dato: ")
        diccionario=[dato]= valor
        print(diccionario)
