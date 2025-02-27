def Cargar():
    ListaArticulos = []
    ListaPrecios = []
    final = 3
    for i in range(final):
        ListaArticulos.append(input("Ingrese nombre del articulo: "))
        ListaPrecios.append(float(input("Ingrese precio del articulo: ")))
    return ListaArticulos,ListaPrecios
def Imprimir(n1,n2):
    for i, articulos in enumerate(n1):
        print(f"Articulo nro {i+1}: {articulos}, precio: {n2[i]}")

def PrecioMayor(n1,n2):
    mayor = 0
    for i, precio in enumerate(n1):
        if precio>mayor:
            mayor=precio
            print(f"El mayor precio es {mayor} que corresponde a {n2[i]}")

ListaArticulos, ListaPrecios = Cargar()
Imprimir(ListaArticulos,ListaPrecios)
PrecioMayor(ListaPrecios,ListaArticulos)
