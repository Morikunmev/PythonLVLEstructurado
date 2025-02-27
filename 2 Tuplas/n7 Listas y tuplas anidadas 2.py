def CargarPais():
    paises = []
    for x in range(5):
        nombre = input("Ingrese el nombre del pais: ")
        cantidad = int(input("Ingrese la cantidad: "))
        paises.append((nombre,cantidad))
    return paises
def Imprimir(paises):
    print("Paises y su poblacion")
    for x, valor in enumerate(paises):
        print(valor[0],valor[1])
def MayorMenor(paises):
    mayor = paises[0][1]
    nombremayor = paises[0][0]
    for i, valor in enumerate(paises):
        if valor[1]>mayor:
            mayor = valor[1]
            nombremayor = valor[0]
    print(f"El pais con mas habitantes es {nombremayor} que son {mayor}")


paises = CargarPais()
Imprimir(paises)
MayorMenor(paises)