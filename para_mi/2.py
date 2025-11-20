saldo = float(1000)
salir = ""
while salir  != "4":
    print("1 Saldo")
    print("2 Ingreso")
    print("3 Reintegro")
    print("4 salir")
    salir = input("¿Que opcion quieres usar?")
    if salir == "1":
        print("El total es:" ,total)
    elif salir == "2":
        ingresar = float(input("Cuanto dinero quieres meter a la cuenta"))
        total = saldo +ingresar
        saldo = total
        print("El total es:" ,total)
    elif salir == "3":
        sacar = float(input("Cuanto dinero quieres meter a la cuenta"))
        total = saldo - sacar
        saldo = total
        print("El total es:" ,total)
    