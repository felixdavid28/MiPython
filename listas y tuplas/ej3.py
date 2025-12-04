#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
#nota que ha sacado en cada asignatura, y después las muestre por pantalla con el
#mensaje En <asignatura> has sacado <nota> donde <asignatura> es
#cada una des las asignaturas de la lista y <nota> cada una de las correspondientes
#notas introducidas por el usuario.
lista=["Matemáticas", "Física","Química", "Historia","Lengua"]
for l in lista:
    nota= float(input("Dime la nota que tienes: " + l)) 
    print(nota)