#Escribir un programa que cree un diccionario de traducción español-inglés. El
#usuario introducirá las palabras en español e inglés separadas por dos puntos, y
#cada par <palabra>:<traducción> separados por comas. El programa debe
#crear un diccionario con las palabras y sus traducciones. Después pedirá una frase
#en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra
#no está en el diccionario debe dejarla sin traducir.
traductor = {}

while True:
    Palabra= input("Indica la palabra de español:inglés") 
    tempA=Palabra.split(":")[0]
    tempB=Palabra.split(":")[1]
    traductor[tempA]= tempB

    pregunta= input("¿Quieres continuar? ")
    if pregunta=="no":
        break
#Traduccion
while True:
    frase= input("¿Qué frase quieres traducir? ")
    fraseSplit=frase.split()

    for i in range(len(fraseSplit)):
        palabraActual = fraseSplit[i]
        if palabraActual in traductor:
            fraseSplit[i]= traductor[palabraActual]

    resultado= " ".join(fraseSplit)
    print(resultado)
    continuar= input("¿Quieres continuar? ").lower()
    if continuar== "no":
        break

