"""Escribir un programa que almacene las asignaturas de un curso 
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en 
una lista y la muestre por pantalla."""
while True:

    lista = input("introduce asignaturas de un curso: ").replace(",","").split(" ")
    print(lista)