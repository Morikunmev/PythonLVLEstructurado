def capicua(cadena):
    iguales = 0
    indice = -1
    for x in range(0,len(cadena)//2):
        if cadena[x]==cadena[indice]:
            iguales = iguales + 1
        indice=indice-1
    if iguales == (len(cadena)//2):
        print("es optima")
    else:
        print("no es capicua")
capicua("neuquen")