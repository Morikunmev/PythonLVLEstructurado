def Cargar():
    lista = []
    for i in range(5):
        valor = int(input(": "))
        lista.append(valor)
    lista = tuple(lista)
    return lista
def MayorMenor(n):
    mayor = 0
    menor = n[0]
    for i, valor in enumerate(n):
        if valor >mayor:
            mayor = valor
        elif valor<menor:
            menor = valor
    return (mayor, menor)

lista = Cargar()
maximo, minimo = MayorMenor(lista)
print("El maximo es: ",maximo)
print("El minimo es: ",minimo)
