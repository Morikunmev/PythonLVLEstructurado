def cargar():
    lista = []
    for i in range(5):
        valor = int(input("Ingrese un valor: "))
        lista.append(valor)
    return lista
def GenerarListas(lista):
    ListaNegativos = []
    ListaPositivos = []
    for i, valor in enumerate(lista):
        if valor<0:
            ListaNegativos.append(valor)
        elif valor>0:
            ListaPositivos.append(valor)
    return [ListaNegativos,ListaPositivos]
def Imprimir(lista):
    for i, valor in enumerate(lista):
        print(valor)
lista = cargar()
listanega, listapos = GenerarListas(lista)
print("Valores positivos")
Imprimir(listapos)
print("Valores negativos")
Imprimir(listanega)