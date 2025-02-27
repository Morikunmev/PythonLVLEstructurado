def AsignacionValores():
    lista = []
    for i in range(3):
        empleado = input("Ingresa el nombre del empleado: ")
        sueldo = int(input("Ingrese el sueldo del empleado: "))
        personal = [empleado,sueldo]
        personal = tuple(personal)
        lista.append(personal)
    return tuple(lista)
def MayorMenoor(lista):
    mayor = lista[0][1]
    mayornombre = lista[0][0]
    menor = lista[0][1]
    menornombre = lista[0][0]
    for i in lista:
        if i[1]>mayor:
            mayor = i[1]
            mayornombre = i[0]
        elif i[1]<menor:
            menor = i[1]
            menornombre = i[0]
    return (mayor, mayornombre, menor, menornombre)

lista = AsignacionValores()
maxmin = MayorMenoor(lista)
print(f"El mayor sueldo es: {maxmin[0]} que pertenece a {maxmin[1]}")
print(f"El menor sueldo es: {maxmin[2]} que pertenece a {maxmin[3]}")