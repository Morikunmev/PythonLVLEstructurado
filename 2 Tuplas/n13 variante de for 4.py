def Cargar():
    productos = []
    for x in range(5):
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        productos.append((nombre,precio))
    return productos
def Imprimir(productos):
    print("Listado de productos y precios")
    for nombre, precio in productos:
        print(nombre, precio)
def Rango(productos):
    for nombre, precio in productos:
        if precio>=10 and precio<=15:
            print(nombre,precio)