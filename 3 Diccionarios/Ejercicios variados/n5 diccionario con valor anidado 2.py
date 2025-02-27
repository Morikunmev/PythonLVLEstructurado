def CargarAgenda():
    diccionario = {}
    lista = []
    continua = "s"
    continua1 = "s"
    while continua == "s":
        fecha = input("fecha: ")
        continua1 = "s"
        while continua1=="s":
            hora = input("hora: ")
            actividad = input("actividad: ")
            comprimido = (hora,actividad)
            lista.append(comprimido)
            continua1 = input("Continuar?: ")
            diccionario[fecha] = [lista]
        continua = input("Agregar otra fecha?: ")
    return diccionario
def Imprimir(agenda):
    for fecha, ListaActividades in agenda.items():
        print(f"Fecha: {fecha}")
        for hora,actividad in ListaActividades[0]:
            print(hora,actividad)

agenda = CargarAgenda()
Imprimir(agenda)