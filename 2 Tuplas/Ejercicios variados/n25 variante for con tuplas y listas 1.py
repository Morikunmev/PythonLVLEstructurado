def CargaEmpleados():
    lista = []
    for i in range(5):
        nombre = input("Ingrese el nombre del empleado: ")
        sueldo = int(input("Ingrese el sueldo del empleado: "))
        lista.append((nombre,sueldo))
    return lista
def Imprimir(lista):
    for i in lista:
        print(i)
def SueldoMayor(lista):
    mayor = lista[0][1]
    nombremayor = lista[0][0]
    for i in lista:
        if i[1]>mayor:
            mayor = i[1]
            nombremayor = i[0]
    print(f"El empleado con mayor sueldo es de {nombremayor} que corresponde a {mayor}")
def SueldoMenor1000(lista):
    print("Sueldos menores a 10000")
    for i in lista:
        if i[1]<10000:
            print(i)

lista = CargaEmpleados()
SueldoMayor(lista)
SueldoMenor1000(lista)