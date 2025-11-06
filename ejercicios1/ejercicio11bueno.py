
deposito_inicial = float(input("Introduce la cantidad de dinero depositada: "))
interes = 0.04
ahorro_1 = deposito_inicial * (1 + interes)
ahorro_2 = ahorro_1 * (1 + interes)
ahorro_3 = ahorro_2 * (1 + interes)

print(f"Ahorros después del primer año: {ahorro_1:.2f} €")
print(f"Ahorros después del segundo año: {ahorro_2:.2f} €")
print(f"Ahorros después del tercer año: {ahorro_3:.2f} €")
