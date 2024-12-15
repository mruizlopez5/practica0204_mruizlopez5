"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha 
sacado en cada asignatura, y después las muestre por pantalla con el mensaje 
En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas 
de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
"""
while True:

    lista = input("introduce asignaturas de un curso: ").replace(",","").split(" ")
    notas = input("Ahora introduce las notas respectivamente de la misma manera: ").replace(",","").split(" ")
    for i in range(len(lista)):
        print("En",lista[i], "has sacado",notas[i])