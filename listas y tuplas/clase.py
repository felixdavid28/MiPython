lista=[]
while True:
    print ("1. Añadir número a la lista")
    print ("2. Añadir número a la lista en una posición")
    print ("3. Longitud de la lista")
    print ("4. Eliminar el ultimo número")
    print ("5. Eliminar numeros")
    print ("6. Contar numeros")
    print ("7. Posiciones de un numeros")
    print ("8. Mostrar números")
    print ("9. Salir")

    Menu= int(input("Elige una opción: "))
    if Menu==9:
        print("Saliendo...")
        break
    elif Menu==1:
        print("opcion1")
        v=int(input("Que numero quieres añadir?:"))
        lista.append(v)
        print(lista)
    elif Menu==3:
        print("opcion3")
        longitud = len(lista)
        print(longitud)
    elif Menu==8:
        for i in range(lista):
            print(i, end=" ")
        print("")
    elif Menu==2:
       num= int(input("Introduce el numero a añadir: "))
       pos = int(input("Introduce la posiscion: "))
       pos = pos +1
       lista.insert(pos,num)
    elif Menu==4:
       lista.pop()
    elif Menu==5:
       n = int(input("Dime el numero a eliminar: "))
       lista.remove(n)
    elif Menu==6:
       lista.count()
    elif Menu==7:
        posicion= int(input("dime un numero"))
        contar= 0
        for numero in lista:
            contador = contador +1
            if numero == posicion:
                print(contador) 