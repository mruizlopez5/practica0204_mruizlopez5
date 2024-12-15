"""
Escribir un programa que pida al usuario una palabra 
y muestre por pantalla si es un palíndromo.
"""
while True:
    muestra = list(input("Introduce palabra para verificar si es un palindromo\n"))
    comp = muestra.copy() #en w3school muestra que esa función copy() para listas crea otra copia para que no se machaque luego con el .reverse() la original, no está en los apuntes de listas pero parece ser una funcion basica de listas
    comp.reverse()
    if comp == muestra:
        print("es un palindromo")
    else: 
        print("no es un palindromo")