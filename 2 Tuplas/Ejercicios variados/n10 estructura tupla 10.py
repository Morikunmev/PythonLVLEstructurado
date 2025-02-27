def Fechadef():
    dia = int(input("Ingrese el dia: "))
    mes = int(input("Ingrese el mes: "))
    año = int(input("Ingrese el año: "))
    return (dia,mes,año)
def ImprimirFecha(n):
    print(f"La fecha ingresada es: {n}")

fecha1 = Fechadef()
ImprimirFecha(fecha1)


