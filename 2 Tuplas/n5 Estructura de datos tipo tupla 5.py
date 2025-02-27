def CargarEmpleado():
    nombre = input("Nombre: ")
    sueldo = input(input("Salario: "))
    return (nombre,sueldo)
def MayorSueldo(empleado1,empleado2):
    if empleado1[1]>empleado2[1]:
        print(empleado1[0]. "tiene el mayor sueldo")
    else:
        print(empleado2[0], "tiene el mayor sueldo")
empleado1 = CargarEmpleado()
empleado2 = CargarEmpleado()
MayorSueldo(empleado1,empleado2)