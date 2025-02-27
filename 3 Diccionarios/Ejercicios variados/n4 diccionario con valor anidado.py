def Cargar():
    diccionario = {}
    for i in range(3):
        codigo = int(input("codigo: "))
        producto = input("producto: ")
        precio = int(input("precio: "))
        cantidad = int(input("cantidad: "))
        comprimido = (producto,precio,cantidad)
        diccionario[codigo]=comprimido
    return diccionario
def Imprimir(n):
    for i, (clave, (producto, precio, cantidad)) in enumerate(n.items()):
        print(f"codigo nro {i+1}: {clave}, producto: {producto} precio: {precio} cantidad: {cantidad}")
productos = Cargar()
Imprimir(productos)