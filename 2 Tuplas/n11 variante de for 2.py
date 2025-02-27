def Cargar():
    empleado = []
    for i in range(5):
        nombre = input("Ingrese el nombre del empleado: ")
        sueldo = int(input("Ingrese el sueldo del empleado: "))
        empleado.append((nombre,sueldo))
    return empleado

def Imprimir(empleados):
    print("Listado de los nombres de empleados y sus sueldos")
    for nombre, sueldo in empleados:
        print(nombre,sueldo)
def MayorSueldo(empleados):
    empleado = empleados[0]
    for emp in empleados:
        if emp[1]>empleado[1]:
            empleado = emp
    print(f"Empleado con mayor sueldo es {empleado[0]} que corresponde a {empleado[1]}")
def SueldoMenor10000(empleados):
    cant = 0
    for empleado in empleados:
        if empleado[1]<10000:
            cant+=1
    print(f"Cantidad de empleados con sueldo menor a 1000 son: {cant}")