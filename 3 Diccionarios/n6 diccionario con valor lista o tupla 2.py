def Cargar():
    agenda = {}
    continua = "s"
    while continua == "s":
        fecha = input("Ingrese una fecha con formato dd/mm/aaaa: ")
        continua2 ="s"
        lista = []
        while continua2 == "s":
            hora = input("Ingrese hora con formato hh/mm: ")
            actividad = input("Ingrese la actividad: ")
            lista.append((hora,actividad))
            continua2 = input("Ingrese otra actividad para la misma fecha: ")
        agenda[fecha]=lista
        continua = input("Ingrese otra fecha: ")
    return agenda
def listado(agenda):
    for fecha in agenda:
        print("Para la fecha", fecha)
        for hora,actividad in agenda[fecha]:
            print(hora,actividad)
def ConsultaFecha(agenda):
    fecha = input("Ingrese la fecha a consultar: ")
    if fecha in agenda:
        for hora, actividad in agenda[fecha]:
            print(hora,actividad)
    else:
        print("No hay")