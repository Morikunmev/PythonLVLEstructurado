def CargarDatos():
    candidatos = []
    for i in range(3):
        nombre = input("Ingrese nombre: ")
        cant = int(input("Los votos de cuantas provincias tiene que cargar: "))
        provincias = []
        for x in range(cant):
            prov = input("Nombre de la provincia: ")
            votos = int(input("Cantidad de votos: "))
            provincias.append((prov,votos))
        candidatos.append((nombre,provincias))
    return candidatos

def TotalVotos(n):
    for i in range(len(n)):
        suma = 0
        for x in range(len(n[i][1])):
            suma = suma + n[i][1][x][1]
        print(n[x][0],suma)

candidatos = CargarDatos()
votos = TotalVotos(candidatos)
