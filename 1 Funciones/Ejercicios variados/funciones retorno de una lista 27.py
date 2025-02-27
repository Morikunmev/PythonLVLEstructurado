def Validar(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            return numero
        except:
            continue

def CargaElementos():
    lista = []
    for i in range(10):
        lista.append(Validar("Ingrese numero entero: "))
    return lista

def TresListas(lista):
    Listapos= []
    Listaneg= []
    Listaneu= []
    for i, valor in enumerate(lista):
        if valor>0:
            Listapos.append(valor)
        elif valor<0:
            Listaneg.append(valor)
        elif valor == 0:
            Listaneu.append(valor)

    return Listapos,Listaneg,Listaneu
def Imprimir3Listas(listapos,listaneg,listaneu):
    print("Valor Positivo")
    for i, valor in enumerate(listapos):
        print(i+1, valor)
    print("Valor negativo")
    for x, valor in enumerate(listaneg):
        print(x+1, valor)
    for y, valor in enumerate(listaneu):
        print(y+1, valor)

lista = CargaElementos()
listapos, listaneg, listaneu = TresListas(lista)
Imprimir3Listas(listapos,listaneg,listaneu)