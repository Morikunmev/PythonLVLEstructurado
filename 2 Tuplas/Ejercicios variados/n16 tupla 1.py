def CargarAlumnos():
    lista = []
    for i in range(2):
        nombre = input("Ingresa nombre: ")
        edad = int(input("Ingresa edad: "))
        calificacion = float(input("Ingresa calificacion: "))
        alumno = [nombre,edad,calificacion]
        alumno = tuple(alumno)
        lista.append(alumno)
    return lista
def Imprimir(registro):
    for i in range(len(registro)):
        print(f"Registro nro {i+1}: nombre: {registro[i][0]}: edad: {registro[i][1]}, calificacion:{registro[i][2]}")
registro = CargarAlumnos()
Imprimir(registro)

def MayorMenor(registro):
    MayorNombre = registro[0][0]
    MayorEdad = registro[0][1]
    MayorCalificacion = registro[0][2]

    MenorNombre = registro[0][0]
    MenorEdad = registro[0][1]
    MenorCalificacion = [0][2]

    for i in registro:
        if i[2]>MayorCalificacion:
            MayorCalificacion = i[2]
            MayorEdad = i[1]
            MayorNombre = i[0]
        elif i[2]<MenorCalificacion:
            MenorCalificacion = i[2]
            MenorEdad = i[1]
            MenorNombre = i[0]
    return (MayorNombre,MenorNombre)
registro = CargarAlumnos()
Imprimir(registro)
mayor_nombre,menor_nombre = MayorMenor(registro)
print(f"El mayor nombre es {mayor_nombre}")
print(f"El menor nombre es: {menor_nombre}")