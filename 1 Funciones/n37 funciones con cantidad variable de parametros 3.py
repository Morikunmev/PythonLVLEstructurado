def CantidadMayores18(edad,*edades):
    cant = 0
    if edad>=18:
        cant+=1
    for i, valor in enumerate(edades):
        cant+=1
    return cant
print("Cantidad de personas mayores de 18 años son")
print(CantidadMayores18(23,2,3,5,123,23,123,2))