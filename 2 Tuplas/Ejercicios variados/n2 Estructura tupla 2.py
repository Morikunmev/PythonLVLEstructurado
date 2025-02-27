def fechadef():
    dia = int(input("Ingrese dia: "))
    mes = int(input("Ingrse mes: "))
    año = int(input("Ingrese año: "))
    return (dia,mes,año)
def imprimir(fecha):
    print(fecha[0],fecha[1],fecha[2],sep="/")

def fechadef1(n1 = 30,n2 = 12,n3 = 1998):
    return (n1,n2,n3)
def conversion(fecha):
    fecha = list(fecha)
    return fecha
def añadir(fecha):
    fecha.append("ajdjadjas")
    fecha.append("No se que poner")
    return fecha
def conversion1(fecha):
    fecha = tuple(fecha)
    return fecha
def empaquetamiento(*n):
    return (n[0],n[1],n[2])


fecha1 = fechadef()
imprimir(fecha1)
fecha2 = fechadef1()
fecha2 = conversion(fecha2)
fecha2 = añadir(fecha2)
fecha2 = conversion1(fecha2)
print(fecha2)

fecha3 = empaquetamiento(30,12,1998)
imprimir(fecha3)