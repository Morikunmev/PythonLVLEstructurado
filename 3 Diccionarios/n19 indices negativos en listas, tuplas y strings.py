def Cargar():
    palabras = []
    for x in range(5):
        pal = input("Ingrese una palabra: ")
        palabras.append(pal)
    return palabras
def Intercambiar(palabras):
    aux = palabras[0]
    palabras[0]=palabras[-1]
    palabras[-1]=aux
def Imprimir(palabras):
    print(palabras)
palabras = Cargar()
Imprimir(palabras)
Intercambiar(palabras)
Imprimir(palabras)