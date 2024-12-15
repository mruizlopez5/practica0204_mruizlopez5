"""
Escribir un programa que pregunte por una muestra de números, 
separados por comas, los guarde en una lista y muestre por 
pantalla su media y desviación típica.
"""
while True:

    ENTRADA = input("introduce numeros enteros separados por comas(comas vacias o finales cuentan como 0):\n").replace(" ","").split(",")
    ENTRADA_int = []
    print("La lista introducida en strings es",ENTRADA)

    #He visto por internet que con la función map(int.....) se podria convertir los elemento de la lista a ints, -
    #-pero me veo en el caso de utilizar el programa que realicé para la mejora de nota ya que no hemos visto dicha funcion.

    for i in ENTRADA:  #ITERO CADA ELEMENTO EMPLEANDO EL CODIGO DEL TRABAJO DE MEJORA DE NOTA PARA CADA -
                       #-ELEMENTO DE LA LISTA CON UNA PEQUEÑA MODIFICACION PARA QUE LO HAGA CON LISTAS
        
        lista = list(i).copy() #modificación en cuestión 1: en cada interación copia cada elemento de -
                               #-la lista y lo hace una lista en si mismo para pasarlo individualmente -
                               #-a int y añadirlo luego la salida "total" a la lista ENTRADA_int
        total = 0

        lista.reverse()

        des = True

        for i in range(len(lista)):
            if "/" < lista[i] < ":" or "," < lista[i] < "." or "*" < lista[i] < ",": #ahora admite también el simbolo +
                ""
            else:  
                des = False

        if des != False:
            for i in range(len(lista)):
                        if lista[i] == "1":
                            total = total + 1*pow(10, i)
                        elif lista[i] == "2":
                            total = total + 2*pow(10, i)
                        elif lista[i] == "3":
                            total = total + 3*pow(10, i)
                        elif lista[i] == "4":
                            total = total + 4*pow(10, i)
                        elif lista[i] == "5":
                            total = total + 5*pow(10, i)
                        elif lista[i] == "6":
                            total = total + 6*pow(10, i)
                        elif lista[i] == "7":
                            total = total + 7*pow(10, i)
                        elif lista[i] == "8":
                            total = total + 8*pow(10, i)
                        elif lista[i] == "9":
                            total = total + 9*pow(10, i)
                        elif lista[i] == "-":
                            total = total*-1
                        elif lista[i] == "+":
                            total = total*1

            ENTRADA_int.append(total)#modificación en cuestion 2: en lugar de -
                                     #-mostrar el resultado, lo añado a la lista

        else: 
            print("sólo números enteros o números negativos enteros")#ADMITE NEGATIVOS!!! no floats...
            
    #EN este punto ya tengo la lista hecha solo de integers
    print("La lista en strings convertida a enteros es",ENTRADA_int)

    #calculo media
    suma = 0
    for i in ENTRADA_int:
        suma = suma + i
    media = suma/len(ENTRADA_int)

    #calculo desviación tipica por partes
    NUMERADORdesv = 0
    for i in ENTRADA_int:
        NUMERADORdesv = NUMERADORdesv + pow((i-media), 2)
    desvT = pow((NUMERADORdesv/len(ENTRADA_int)),(1/2)) #hago la raiz elevando a 1/2

    print("Media de los valores intorudcidos:", round(media,2))
    print("Desviación tipica de los valores intorudcidos:", round(desvT,2))