def CargarEmpleados():
    lista = []
    for i in range(2):
        nombre = input("Ingrese el nombre del empleado: ")
        sueldo1 = int(input("Ingrese el sueldo 1: "))
        sueldo2 = int(input("Ingrese el sueldo 2: "))
        sueldo3 = int(input("Ingrese el sueldo 3: "))
        lista.append([nombre,(sueldo1,sueldo2,sueldo3)])
    return lista
def Imprimir(registro):
    for i, valor in enumerate(registro):
        print(valor[0],valor[1])
def ImprimirMas(registro):
    for i, suma in enumerate(registro):
        print(suma[0],sum(suma[1]))
def Mayor10000(registro):
    print("Ingreso trimestral mayor a 10000")
    for i,sueldo in enumerate (registro):
        if sum(sueldo[1])>10000:
            print(sueldo)

registro = CargarEmpleados()
Imprimir(registro)
print()
ImprimirMas(registro)
print()
Mayor10000(registro)
