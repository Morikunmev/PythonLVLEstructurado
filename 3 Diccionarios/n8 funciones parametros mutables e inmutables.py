def Cargar():
    lista = []
    continua = "s"
    while continua == "s":
        valor = int(input("Ingrese valor: "))
        lista.append(valor)
        continua = input("CONTINUA?: ")
    return lista
def FijarCero(lista):
    for i,valor in enumerate (lista):
        if valor<10:
            lista[i] = 0
    print(lista)
numeros = Cargar()
FijarCero(numeros)

