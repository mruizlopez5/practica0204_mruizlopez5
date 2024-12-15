"""
Escribir un programa que almacene el abecedario en una lista, elimine de la 
lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla 
la lista resultante.
"""
abc = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
abc2 = []
z=0
for i in abc:
    z+=1
    if z%3 != 0:
        abc2.append(i)
print(abc2)