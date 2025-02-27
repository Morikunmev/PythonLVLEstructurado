def CargarEmpleados():
    empleados = []
    for x in range(5):
        nombre = input("Ingrese el nombre del empleado: ")
        sueldo1 = int(input("Ingrese el primer sueldo: "))
        sueldo2 = int(input("Ingrese el segundo sueldo: "))
        sueldo3 = int(input("Ingrese el tercer sueldo: "))
        empleados.append([nombre,(sueldo1,sueldo2,sueldo3)])
    return empleados
def Ganancias(empleados):
    print("Monto total ganado por empleado en los ultimos 3 meses")
    for i in range(5):
        total = empleados[i][1][0]+empleados[i][1][1]+empleados[i][1][2]
        print(empleados[i][0],total)
def GananciaSuperior(empleados):
    print("Empleados con ingresos superiores a 10000 en los ultimos 3 meses")
    for i in range(5):
        total = empleados[i][1][0]+empleados[i][1][1]+empleados[i][1][2]
        if total >10000:
            print(empleados[x][0],total)

empleados = CargarEmpleados()
Ganancias(empleados)
GananciaSuperior(empleados)