def Cargar():
    productos = {}
    continua = "s"
    while continua=="s":
        codigo = int(input("codigo: "))
        descripcion = input("descripcion: ")
        precio = float(input("precio: "))
        stock = int(input("stock: "))
        productos[codigo] = (descripcion,precio,stock)
        continua = input("Desea cargar otro producto?: ")
    return productos
def Imprimir(productos):
    for codigo in productos:
        print(codigo, productos[codigo][0], productos[codigo][1], productos[codigo][2])

def Consulta(productos):
    codigo = int(input("CONSULTA: "))
    if codigo in productos:
        print(productos[codigo][0],productos[codigo][1],productos[codigo][2])
def ListadoStockCero(productos):
    for codigo in productos:
        if productos[codigo][2]==0:
            print(codigo,productos[codigo][0],productos[codigo][1])

productos = Cargar()
Imprimir(productos)
Consulta(productos)
ListadoStockCero(productos)