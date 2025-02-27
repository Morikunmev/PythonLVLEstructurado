def CargaValores():
    lista = []
    for i in range(5):
        producto = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        lista.append((producto,precio))
    return lista
def Imprimir(productos):
    for producto, precio in productos:
        print(producto,precio)
def Rango(productos):
    print("Productos comprendidos entre 10 y 15")
    for i in productos:
        if i[1]>=10 and i[1]<=15:
            print(i)
productos = CargaValores()
Imprimir(productos)
Rango(productos)
