num =int(input("Di un número"))
suma = num
mayor= num
menor= num
for i in range(1,6):
    num=int(input("Di un numero"))
    suma = suma + num
    if mayor < num:
        mayor = num
    if menor < num:
        menor = num

print("La suma total es: ", suma)
print("La suma total es: ", mayor)
print("La suma total es: ", menor)