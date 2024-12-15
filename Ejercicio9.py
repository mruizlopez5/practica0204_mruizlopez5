"""
Escribir un programa que pida al usuario una palabra y muestre 
por pantalla el número de veces que contiene cada vocal.
"""
while True:
    
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0

    palabra = list(input("introduce palabra: ").lower())

    for z in palabra:
        if "a" == z:
            a += 1 
        if "e" == z:
            e += 1 
        if "i" == z:
            i += 1 
        if "o" == z:
            o += 1 
        if "u" == z:
            u += 1 

    valor = [a, e, i, o, u]
    vocales = ["a", "e", "i", "o", "u"]

    for i in range(len(vocales)):
        if valor[i] == 1:
            print(vocales[i], "aparece", valor[i], "vez")
        elif valor[i] > 1:
            print(vocales[i], "aparece", valor[i], "veces")