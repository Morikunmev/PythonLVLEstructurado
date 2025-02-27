def CargarDatos():
    estudiantes = {}
    for i in range(2):
        nombre = input("Ingrese el nombre del estudiante: ")
        edad = int(input("Ingrese la edad del estudiante: "))
        estudiantes[nombre]=edad
    return estudiantes
def Imprimir(estudiantes):
    for clave, valor in estudiantes.items():
        print(clave,valor)
def maxmin(estudiantes):
    mayor = 0
    nombre = ""
    for clave, valor in estudiantes.items():
        if valor>mayor:
            nombre = clave
            mayor = valor
    return nombre, mayor

estudiantes = CargarDatos()
Imprimir(estudiantes)
print(maxmin(estudiantes))