def CargarPalabras():
    lista = []
    for i in range(5):
        palabra = input("Ingresa una palabra")
        lista.append(palabra)
    return lista
def Masde5Caracteres(palabras):
    print("Mas de 5 palaras")
    for i in palabras:
        if len(i)>5:
            print(i)

palabras = CargarPalabras()
Masde5Caracteres(palabras)