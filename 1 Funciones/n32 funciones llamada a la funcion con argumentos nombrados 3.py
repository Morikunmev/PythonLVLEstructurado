def Cargar():
    lista = []
    for i in range(4):
        lista.append(int(input("Ingrese: ")))
    return lista
def Imprimir(lista):
    for i, valor in enumerate(lista):
        print(valor,end="-")
lista = Cargar()
Imprimir(lista)
