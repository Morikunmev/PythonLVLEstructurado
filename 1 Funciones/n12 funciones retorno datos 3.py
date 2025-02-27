def largo(cadena):
    return len(cadena)
#Bloque principal

nombre1 = input("Ingrese primer nombre: ")
nombre2 = input("Ingrese segundo nombre: ")
largo1 = largo(nombre1)
largo2 = largo(nombre2)
if largo1 == largo2:
    print("Los nombres tienen la misma cantidad de caracteres")
elif largo1>largo2:
    print(nombre1,"Es mas largo")
elif largo2>largo1:
    print(nombre2,"Es mas largo")
