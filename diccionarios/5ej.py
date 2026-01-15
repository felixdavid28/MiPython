#Escribir un programa que almacene el diccionario con los créditos de las asignaturas
#de un curso {'Matemáticas': 6, 'Física': 4, 'Química': 5} y después
#muestre por pantalla los créditos de cada asignatura en el formato <asignatura>
asignaturas ={
    "matematicas": "6",
    "fisica": "4",
    "quimica": "5"
}
suma= 0
for asignaturas, creditos in asignaturas.items():
    print(f"{asignaturas} tiene {creditos} créditos")  
    suma += int(creditos)
print(f"la suma de creditos es: {suma}")