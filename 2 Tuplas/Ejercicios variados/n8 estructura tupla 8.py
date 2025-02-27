def CargaDatos():
    nombres = []
    sueldos = []
    for i in range(5):
        nombre = input("Ingrese nombre: ")
        sueldo = int(input("Ingrese sueldo: "))
        nombres.append(nombre)
        sueldos.append(sueldo)
    nombres = tuple(nombres)
    sueldos = tuple(sueldos)
    return nombres, sueldos

def MayorSueldodef(n1,n2):
    MayorSueldo = 0
    MayorNombre = 0
    for i, valor in enumerate(n1):
        if valor>MayorSueldo:
            MayorSueldo = valor
            MayorNombre = n2[i]
    return MayorSueldo, MayorNombre


nombres, sueldos = CargaDatos()
MayorSueldo, MayorNombre = MayorSueldodef(sueldos,nombres)
print(f"El mayor sueldo es: {MayorSueldo} que pertenece a {MayorNombre}")