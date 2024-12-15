"""
Escribir un programa que almacene las matrices:

A = [1, 2, 3]
    [4, 5, 6]

B = [-1, 0]
    [0, 1]
    [1, 1]
	
en una lista y muestre por pantalla su producto.
A x B =A11*B11+A12*B21+A13*B31 , 
Nota: Para representar matrices mediante listas usar listas anidadas, representando cada vector fila en una lista.
"""
A = [
    [1, 2, 3],
    [4, 5, 6]
]
B = [
    [-1, 0],
    [0, 1],
    [1, 1]
]

mA=len(A)#mido elementos de A(osease el nuemero de filas)
nA= len(A[0]) #mido numero de columnas en A(elementos dentronde una fila)

mB=len(B)
nB=len(B[0])

print("La matriz A tiene", mA, "filas y", nA, "columnas")
print("La matriz B tiene", mB, "filas y", nB, "columnas")

AxB=0
for z in range(mA):
	
	for i in range(nA):
		C=A[z][i]*B[i][z]
		AxB=AxB+C
		print("En este paso el resultado de A" + str(z+1) + str(i+1) + "(" + str(A[z][i]) + ")", "por B" + str(i+1) + str(z+1) + "(" + str(B[i][z]) + ")", "=", C)
		
print("La suma de todos los pasos por ende el producto de las matries AxB =", AxB)

#me ha llevado demsaido tiempo sacar esto para que quede bonito y poder comprobarlo a la vez xd, -
#-estaria crema poder modificarlo para que el usuario defina las matrices a y b y que compruebe si Am=Bn y que Bm=An