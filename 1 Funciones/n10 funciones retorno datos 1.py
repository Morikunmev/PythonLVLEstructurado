def RetornarSuperficie(lado):
    superficie = lado*2
    return superficie

#Bloque principal
lado = int(input("Ingresa el valor del cuadrado: "))
superficie = RetornarSuperficie(lado)
print(f"La superficie del cuadrado es: {superficie}")

lado = int(input("Ingresa el valor del cuadrado: "))
print("La superficie del cuadrado es: ",RetornarSuperficie(lado))

lado = int(input("Ingresa el valor del cuadrado: "))
if RetornarSuperficie(lado) == 100:
    print("La superficie es 100")
else:
    print("La superficie no es 100")
