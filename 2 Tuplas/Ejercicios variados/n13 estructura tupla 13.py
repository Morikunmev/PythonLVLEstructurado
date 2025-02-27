def CargaPersonal():
    nombre = input("Ingrese su nombre: ").capitalize()
    sueldo = int(input("Ingrese su sueldo: "))
    return (nombre, sueldo)
def Imprimir(n):
    for i,valor in enumerate(n):
        print(f"Registro nro {i+1}: Nombre: {valor[0]}, Sueldo: {valor[1]}")
def Empaquetamiento(*n):
    return n
def MayorMenor(n):
    mayor = n[0]
    menor = n[0]
    for valor in n:
        if valor[1]>mayor[1]:
            mayor = valor
        elif valor[1]<menor[1]:
            menor = valor
    return (mayor,menor)
empleado1 = CargaPersonal()
empleado2 = CargaPersonal()
empleado3 = CargaPersonal()
empleado4 = CargaPersonal()

TuplaGeneral = Empaquetamiento(empleado1,empleado2,empleado3,empleado4)
print(MayorMenor(TuplaGeneral))