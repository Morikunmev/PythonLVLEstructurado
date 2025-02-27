def Cargar(cadena):
    cant = 0
    evaluar = input(cadena)
    for i in evaluar:
        if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
            cant+=1
    print(f"La cantidad de volcales son: {cant}")
for i in range(3):
    Cargar("Ingresa ctm: ")