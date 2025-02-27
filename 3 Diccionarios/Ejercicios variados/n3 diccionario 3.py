def CargarDocumento():
    documento = {}
    bucle = "s"
    while bucle=="s":
        numero = int(input("Ingrese el numero de documento: "))
        nombre = input("Ingrese el nombre de la persona: ")
        documento[numero]=nombre
        bucle = input("Quiere agregar mas clientes s/n: ")
    return documento
def Imprimir(documento):
    for i, (clave,valor) in enumerate(documento.items()):
        print(f"Registro nro {i+1}: {clave}, {valor}")
def Consulta(documento):
    consulta = int(input("Ingrese el documento a consultar: "))
    if consulta in documento:
        print(f"su nombre es: {documento[consulta]}")
    else:
        print("No encontrado")
documento = CargarDocumento()
Imprimir(documento)
Consulta(documento)
