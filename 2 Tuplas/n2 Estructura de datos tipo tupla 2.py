def CargarFecha():
    dia = int(input("Ingresar dia: "))
    mes = int(input("Ingresar mes: "))
    año = int(input("Ingresar año: "))
    return (dia, mes, año)

def ImprimirFecha(fecha):
    print(fecha[0],fecha[1],fecha[2],sep="/")

fecha = CargarFecha()
ImprimirFecha(fecha)
lista = list(fecha)
