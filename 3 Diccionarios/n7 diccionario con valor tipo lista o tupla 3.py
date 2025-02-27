def Cargar():
    alumnos = {}
    for x in range(3):
        dni = int(input("Ingrese numero de dni: "))
        listamaterias = []
        continua= "s"
        while continua == "s":
            materia = input("Ingrese el nombre de la materia: ")
            nora = int(input("Ingrese la nota: "))
            listamaterias.append((materia,nora))
            continua =input("Desea cargar otra materia para dicho alumno?: ")
        alumnos[dni]=listamaterias
    return alumnos
def Listar(alumnos):
    for dni in alumnos:
        print("Dni del alumno: ",dni)
        for nota, materia in alumnos[dni]:
            print(nota,materia)
def ConsultaNotas(alumnos):
    dni = int(input("Ingrese el dni a consultar: "))
    for dni in alumnos:
        for materia, nota in alumnos[dni]:
            print(materia,nota)

alumnos = Cargar()
Listar(alumnos)
ConsultaNotas(alumnos)