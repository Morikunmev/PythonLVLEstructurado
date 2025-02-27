#Tienda de productos

def CargarProductos():
    tupla = []
    for i in range(3):
        nombre = input(f"Ingresa producto {i+1} / 3: ")
        precio = int(input(f"Ingrese precio {i+1} / 3: "))
        stock = int(input(f"Ingrese cantidad {i+1} / 3: "))
        producto = nombre,precio,stock
        tupla.append(producto)
    return tuple(tupla)
def CaroBarato(productos):
    NombreMayor = productos[0][0]
    PrecioMayor = productos[0][1]
    StockMayor = productos[0][2]

    NombreMenor = productos[0][0]
    PrecioMenor = productos[0][1]
    StockMenor = productos[0][2]

    for i, valor in enumerate(productos):
        if valor[1]>PrecioMayor:
            NombreMayor = valor[0]
            PrecioMayor = valor[1]
            StockMayor = valor[2]
        elif valor[1]<PrecioMenor:
            NombreMenor = valor[0]
            PrecioMenor = valor[1]
            StockMenor = valor[2]
    return (NombreMayor,PrecioMayor,StockMayor,NombreMenor,PrecioMenor,StockMenor)

productos = CargarProductos()
print(productos)
NombreMayor,PrecioMayor,StockMayor,NombreMenor,PrecioMenor,StockMenor = CaroBarato(productos)
print(f"El producto mas caro es {NombreMayor} que es {PrecioMayor} con cantidad {StockMayor}")
print(f"El producto menos caro es {NombreMenor} que es {PrecioMenor} con cantidad {StockMenor}")