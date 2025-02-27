def mascaracteres(lista):
    pos = 0
    for i in range(1,len(lista)):
        if len(lista[i])>len(lista[pos]):
            pos =i
    return lista[pos]

palabras = ["enero","febrero","marzo","abril","mayo","junio"]
print(f"Palabra con mas caracteres: {mascaracteres(palabras)}")