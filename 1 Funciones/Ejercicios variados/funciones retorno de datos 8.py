final = 4
mayor = ""
for i in range(final):
    nombre = input(f"Ingresa un nombre {i+1}/{final}")
    if len(nombre)> len(mayor):
        mayor = nombre
print(mayor)