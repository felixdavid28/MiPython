
cantidad = float(input("Introduce la cantidad a invertir: "))
interes = float(input("Introduce el interés anual: "))
años = int(input("Introduce el número de años: "))

final = cantidad * (1 + interes / 100) ** años
print(f"El capital obtenido tras {años} años es: {final} €")