def cargar():
    empleados = {}
    continua = "s"
    while continua == "s":
        legajo = int(input("Ingrese el nombre de legajo"))
        nombre = input("nombre: ")
        profesion = input("profecion: ")
        sueldo = float(input("sueldo: "))
        empleados[legajo]=[nombre,profesion,sueldo]

        continua = input("Quiere la carga de otro empleado: ")
    return empleados
def Imprimir(empleados):
    for clave in empleados:
        print(clave, empleados[clave][0],empleados[clave][1],empleados[clave][2])
def Modificar(empleados):
    buscar = int(input("Ingrese el legajo a modificar: "))
    if buscar in empleados:
        sueldo = float(input("Ingrese nuevo sueldo: ")
        empleados[buscar][2]=sueldo
    else:
        print("No existe")
def ImprimirAnalistas(empleados):
    print("todos los analistas")
    for i in empleados:
        if empleados[1]=="Analista":
            print(i,empleados[i][0],empleados[i][2])
