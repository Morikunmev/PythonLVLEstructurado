def cargar():
    ListaArticulos = []
    ListaPrecios = []
    final = 3
    for i in range(final):
        ListaArticulos.append(input(f"Ingrese el nombre del acticulo nro {i+1} de {final}: "))
        ListaPrecios.append(float(input(f"Ingrese el precio del articulo {i+1}/{final}: ")))
    return ListaArticulos,ListaPrecios
def Imprimir(n1,n2):
    for i, art in enumerate(n1):
        print(f"Articulo nro {i+1}: {art}, precio: {n2[i]}")

def PrecioMayor(n):
    mayor = 0
    repetidos = []
    for i, precio in enumerate(n):
        if precio>mayor:
            mayor = precio
        elif precio == mayor:
            repetidos.append(precio)
    repetidos.append(mayor)
    return mayor, repetidos

ListaArticulos, ListaPrecios = cargar()
Imprimir(ListaArticulos,ListaPrecios)
MayorPrecio, ListaRepetidos = PrecioMayor(ListaPrecios)
print(f"El precio mayor es {MayorPrecio}")
print(f"La lista de repetidos son: {ListaRepetidos}")
print(f"Cantidad de valores mayores repetidos es {len(ListaRepetidos)}")