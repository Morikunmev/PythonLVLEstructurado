def CargaDatos():
    ListaNombres= []
    ListaEdad =[]
    final = 3
    for i in range(final):
        ListaNombres.append(input(f"Ingrese el nombre {i+1}/{final}: "))
        ListaEdad.append(int(input(f"Ingrese la edad {i+1}/{final}: ")))

    return ListaNombres,ListaEdad
def ImprimirMayor(nombres,edades):
    for i in range(len(nombres)):
        if edades[i]>=18:
            print(f"Nombre nro {i+1}: {nombres[i]}, edad = {edades[i]}")
def EdadMasAlta(nombres,edades):
    NombreAlto = nombres[0]
    EdadAlta = edades[0]
    Lista1=[]
    Lista2=[]
    for i in range(len(nombres)):
        if edades[i]>EdadAlta:
            EdadAlta = edades[i]
            NombreAlto = nombres[i]
        elif edades[i] == EdadAlta:
            Lista1.append(nombres[i])
            Lista2.append(edades[i])

    print(f"La edad mas alta es: {NombreAlto}  que es {EdadAlta}")
    print("lista de nombres repetidos")
    for i in range(len(Lista1)):
        print(Lista1[i],Lista2[i])

Nombres,Edades = CargaDatos()
ImprimirMayor(Nombres,Edades)
EdadMasAlta(Nombres,Edades)
