from mod1 import empleados
#Registro de empleados
def CargarDatos():
    registro = []
    final = int(input("Catos empleados a registrar?: "))
    for i in range(final):
        nombre = input(f"Ingresa el nombre del empleado {i+1} / {final}: ")
        salario = int(input(f"Ingrese el salario del empleado {i+1}/ {final}: "))
        departamento = input(f"Ingresa el nombre del departamento {i+1} / {final}: ")
        empaquetado = (nombre,salario,departamento)
        registro.append(empaquetado)
    return tuple(registro)

RegistroGeneral = CargarDatos()
empleados.Imprimir(RegistroGeneral)
mayor,menor = empleados.MayorMenor(RegistroGeneral)
print(f"El mayor sueldo es {mayor}")
print(f"El menor sueldo es {menor}")
