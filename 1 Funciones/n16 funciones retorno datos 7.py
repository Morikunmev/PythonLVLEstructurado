def cantidad_vocales(palabras):
    cant = 0
    for x in range(len(palabras)):
        if palabras[x]== "a" or palabras[x]=="A":
            cant = cant + 1
    return cant

palabra = input("Ingrese una palabra: ")
print("La palara", palabra, "tiene",cantidad_vocales(palabra))