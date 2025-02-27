def CargarDatos():
    nombres = []
    edades = []
    final = 5
    for i in range(final):
        nombre = input(f"Ingrese el nombre de las personas {i+1}/{final}: ")
        edad = int(input(f"Ingrese la edad de las personas {i+1}/{final}: "))
        nombres.append(nombre)
        edades.append(edad)
    return nombres,edades

def MayorEdad(nombres,edades):
    print("Personas mayores de edad")
    for i in range(len(nombres)):
        if edades[i]>=18:
            print(nombres[i])
def PromedioEdades(edades):
    suma = 0
    for i in range(len(edades)):
        suma+=edades[i]
    promedio = suma / 5
    print(f"Edad promedio de las personas {promedio}")
nombres, edades = CargarDatos()
MayorEdad(nombres,edades)
PromedioEdades(edades)
