def CargarElementos():
    ListaNombre = []
    ListaEdad = []
    final = 2
    for i in range(final):
        nombre = input(f"Ingresa el nombre de {i+1} / {final}: ")
        edad = int(input(f"Ingrese la edad de {i+1} / {final}: "))
        ListaNombre.append(nombre)
        ListaEdad.append(edad)
    return ListaNombre, ListaEdad

def MayoresDeEdad(n1,n2):
    listaEdad = []
    listaNombre = []
    for i in range(len(n1)):
        if n1[i]>=18:
            listaEdad.append(n1[i])
            listaNombre.append(n2[i])
    return listaEdad,listaNombre
def Imprimir(n1,n2):
    for i in range(len(n1)):
        print(f"Registro nro {i+1}: {n1[i]}, {n2[i]}")
def EdadPromedio(n1):
    suma = 0
    for i in range(len(n1)):
        suma+=n1[i]
    promedio = suma / len(n1)
    return promedio
def ImprimirPromedio(n1):
    print(f"El promedio de las edades es {n1}")

ListaNombre,ListaEdad = CargarElementos()
EdadAlta, NombreAlto = MayoresDeEdad(ListaEdad,ListaNombre)
Imprimir(NombreAlto,EdadAlta)
promedio = EdadPromedio(ListaEdad)
ImprimirPromedio(promedio)

