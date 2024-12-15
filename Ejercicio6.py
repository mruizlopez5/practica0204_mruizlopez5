"""
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha 
sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final 
el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
"""

lista = input("introduce asignaturas de un curso: ").replace(",","").split(" ")
notas = []
lista2 = []
for i in lista:
    print("introduce la nota que has sacado en",i)
    notikens = int(input(""))
    notas.append(notikens)

for i in range(len(notas)):
    if notas[i]<5:
        lista2.append(i)
print(lista2)