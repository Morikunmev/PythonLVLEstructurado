def Cargar():
    persona = {}
    for x in range(4):
        numero = int(input("Ingrese el numero de documento: "))
        nombre = input("Ingrese el nombre de la persona: ")
        persona[numero]=nombre
    return persona
def Imprimir(personas):
    for numero in personas:
        print(numero,personas[numero])
def ConsultaNumero(personas):
    consulta = int(input("Ingrese el numero de documento a consultar: "))
    if consulta in personas:
        print(f"Numero de la persona {personas[consulta]}")
    else:
        print("No existe una persona con dicho numero de nacimiento")

personas = Cargar()
Imprimir(personas)
ConsultaNumero(personas)