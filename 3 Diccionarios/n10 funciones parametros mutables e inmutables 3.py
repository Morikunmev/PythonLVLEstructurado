def Cargar():
    contactos = {}
    continua = "s"
    while continua == "s":
        nombre = input("Nombre: ")
        telefono = int(input("Numero: "))
        contactos[nombre]=telefono
        continua = input("continuar?: ")
    return contactos
def ModificarContacto(contactos):
    nombre = input("Ingrese el nombre de contacto a modificar: ")
    if nombre in contactos:
        telefono = input("Ingrese el nuevo numero: ")
        contactos[nombre]=telefono
    else:
        print("No existe un contacto con el nombre ingresado")
def Imprimir(contacto):
    for i in contacto:
        print(i,contacto[i])

contacto = Cargar()
Imprimir(contacto)
ModificarContacto(contacto)
Imprimir(contacto)