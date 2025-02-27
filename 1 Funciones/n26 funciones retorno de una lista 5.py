def CargarDatos():
    articulos = []
    precios = []
    for i in range(3):
        articulos.append(input("Ingrese el nombre del articulo: "))
        precios.append(int(input("Ingrese el precio del articulos: ")))
    return [articulos,precios]
def Imprimir(articulos,precios):
    print("Listado completo de articulos y precios")
    for i,articulo in enumerate(articulos):
        print(articulo, precios[i])
def PrecioMayor(articulos,precios):
    mayor = 0
    nombre = 0
    for i, precio in enumerate(precios):
        if precio>mayor:
            mayor = precio
            nombre = articulos[i]
    print(f"Articulo con un precio mayor es: {nombre} que es: {mayor}")
def ConsultaPrecio(articulos,precios):
    valor = int(input("Ingrese un importe para mostrar los articulos con un precio menor: "))
    for i, precio in enumerate(precios):
        if precio<=valor:
            print(articulos[i], precio)

articulos, precios = CargarDatos()
Imprimir(articulos,precios)
PrecioMayor(articulos,precios)
ConsultaPrecio(articulos,precios)