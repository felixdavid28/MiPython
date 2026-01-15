#Escribir un programa que guarde en una variable el diccionario {'Euro':'€',
#'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su
#símbolo o un mensaje de aviso si la divisa no está en el diccionario.
dic = {'Dollar': '$', 'Yen':'¥'}
h=input("Dime la divisa")
if h in dic:
    print(dic[h])
else:
    print("No se encuentra  la divisa")