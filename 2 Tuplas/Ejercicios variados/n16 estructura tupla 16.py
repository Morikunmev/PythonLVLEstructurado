#Registro de equipos
def CargarDatos():
    lista = []
    for i in range(5):
        nombre = input(F"Ingrese el nombre {i+1} / 5: ")
        puntuacion = float(input(f"Ingrese la puntuacion {i+1} / 5: "))
        equipo = (nombre, puntuacion)
        lista.append(equipo)
    return lista
def Imprimir(lista):
    for i, valor in enumerate(lista):
        print(f"Registro nro {i+1}: nombre: {valor[0]}, puntuacion: {valor[1]} ")
def MayorMenor(lista):
    MayorNombre = lista[0][0]
    MayorCalificacion = lista[0][1]

    MenorNombre = lista[0][0]
    MenorCalificacion = lista[0][1]
    for i in lista:
        if i[1]>MayorCalificacion:
            MayorCalificacion = i[1]
            MayorNombre = i[0]
        elif i[1]<MenorCalificacion:
            MenorCalificacion = i[1]
            MenorNombre = i[0]
    return (MayorNombre,MayorCalificacion,MenorNombre,MenorCalificacion)
lista = CargarDatos()
Imprimir(lista)
MayorNombre,MayorCalificacion,MenorNombre,MenorCalificacion = MayorMenor(lista)
print(f"La mayor puntuacion es de: {MayorNombre} que son {MayorCalificacion} puntos")
print(f"La menor puntuacion es de: {MenorNombre} que son {MenorCalificacion} puntos")