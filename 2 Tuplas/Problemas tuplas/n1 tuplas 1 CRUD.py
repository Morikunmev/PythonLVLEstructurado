#Productos electronicos

def Registrodef():
    registro = (("jurel",900,"Paramy"),("perro",22999,"wits"),("trutro",2290,"seara"),
                ("bocadillos",900,"granix"))
    return registro
def Consulta(registro):
    consulta = input("Ingrese el producto a consultar: ")
    for i in registro:
        if consulta in i[0] or consulta in i[2]:
            print(i)
def Eliminar(registro):
    registro = list(registro)
    for x in registro:
        print(x)
    eliminar = input("Ingrese el producto a eliminar: ")
    for i in registro:
        if eliminar in i[0] or eliminar in i[2]:
            registro.remove(i)
    registro = tuple(registro)
    print(registro)
    return registro

def Añadir(registro):
    registro = list(registro)
    for i in registro:
        print(i)
    final = int(input("Cuantos quieres añadir?: "))
    for x in range(final):
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        marca = input("Ingrese la marca del producto: ")
        comprimido = (nombre,precio,marca)
        registro.append(comprimido)
    registro = tuple(registro)
    for c in registro:
        print(c)
    return registro



registro = Registrodef()
#registro = Eliminar(registro)
registro = Añadir(registro)