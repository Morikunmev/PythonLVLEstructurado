def Cargar():
    lista = []
    for i in range(10):
        numero = int(input(f"numero {i+1}: "))
        lista.append(numero)
    return lista
def RetornarMitad(lista):
    mitad = len(lista) // 2
    return lista[:mitad]
def Imprimir(lista):
    print(lista)
lista = Cargar()
lista2 = RetornarMitad(lista)
Imprimir(lista)
Imprimir(lista2)