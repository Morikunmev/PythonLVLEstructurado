def Cargar():
    productos = {}
    for i in range(5):
        nombre = input("Ingrese nombre: ")
        precio = int(input("Ingrese el precio: "))
        productos[nombre]=precio
    return productos
def Imprimir(productos):
    print("Listado de todos los producotos")
    for i, (clave,valor) in enumerate(productos.items()):
        print(f"registro nro {i+1}, producto: {clave}, precio {valor}")
def Imprimir1(productos):
    for i in productos:
        print(i, productos[i])

def ImprimirMayores100(productos):
    for i in productos:
        if productos[i]>100:
            print(i)
productos = Cargar()
Imprimir1(productos)
ImprimirMayores100(productos)