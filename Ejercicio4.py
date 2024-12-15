"""
Escribir un programa que pregunte al usuario los números ganadores 
de la lotería primitiva, los almacene en una lista y los muestre 
por pantalla ordenados de menor a mayor.
"""
while True:

    prize = list(input("introduce los numeros del boleto que ha ganao la primitiva"))
    prize.sort()
    print(prize)