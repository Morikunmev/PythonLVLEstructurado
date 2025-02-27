listanombres = []
final = 3
for i in range(final):
    listanombres.append(input(f"Ingresa un nombre {i+1}/ {final}: "))

mayor = ""
for x in range(len(listanombres)):
    if len(listanombres[x])> len(mayor):
        mayor = listanombres[x]
print(f"{mayor} es el nombre mas largo")