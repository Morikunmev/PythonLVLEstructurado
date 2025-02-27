def CargaSueldos():
    ListaSueldos = []
    final = 4
    for i in range(final):
        ListaSueldos.append(int(input(f"Ingrese el sueldo de la persona {i+1} de {final}: ")))
    return ListaSueldos
def ImprmirSueldos(n):
    for i,sueldo in enumerate(n):
        print(f"Registro nro {i+1}: {sueldo}")
def SueldoSuperior(n):
    cant = 0
    for i, sueldo in enumerate(n):
        if sueldo>4000:
            cant+=1
    return cant
def PromedioSueldos(n):
    suma = 0
    for i, sueldo in enumerate(n):
        suma+=sueldo
    promedio = suma / len(n)
    return promedio
def ImprimirDebajo(n,n1):
    lista = []
    for i,sueldo in enumerate(n1):
        if sueldo<n:
            lista.append(sueldo)
    return lista


ListaSueldos = CargaSueldos()
ImprmirSueldos(ListaSueldos)
print(f"Sueldos superiores a 4000: {SueldoSuperior(ListaSueldos)}")
promedio = PromedioSueldos(ListaSueldos)
print(f"El promedio de los sueldos es: {promedio}")
print(f"Lista en linea recta de los sueldos menor al promedio: {ImprimirDebajo(promedio,ListaSueldos)}")



