def CargarSueldos():
    sueldos = []
    for i in range(10):
        sueldo = int(input("Ingrese el sueldo: "))
        sueldos.append(sueldo)
    return sueldos
def ImprimirSueldos(n):
    print("Listado de sueldos")
    for x, sueldo in enumerate(n):
        print(x+1,sueldo)
def SueldoMayor4000(n):
    cant = 0
    for i, sueldo in enumerate(n):
        if sueldo>4000:
            cant+=1
    print(f"Cantidad de sueldos mayor a 4000 {cant}")

def Promedio(sueldos):
    suma = 0
    for i, sueldo in enumerate(sueldos):
        suma +=sueldo
    promedio = suma / len(sueldos)
    return promedio
def SueldoBajo(sueldos):
    pro = Promedio(sueldos)
    print(f"Sueldo promedio de los empleados: {pro}")
    print("Sueldo inferiores al promedio")
    for i, sueldo in enumerate(sueldos):
        if sueldo<pro:
            print(sueldo)

sueldos = CargarSueldos()
ImprimirSueldos(sueldos)
SueldoMayor4000(sueldos)
SueldoBajo(sueldos)