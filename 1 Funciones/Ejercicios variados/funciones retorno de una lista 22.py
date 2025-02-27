def ValoresPorAsignacion():
    lista = [2,4,5,3,2,2,2]
    return lista
def OrdenamientoMayor(n):
    for i in range(len(n)-1):
        for x in range((len(n)-1)-i):
            if n[x]>n[x+1]:
                n[x],n[x+1] = n[x+1],n[x]

    return n

def OrdenamientoMenor(n):
    for i in range(len(n)-1):
        for x in range((len(n)-1)-i):
            if n[x]<n[x+1]:
                n[x],n[x+1] = n[x+1],n[x]
    return n

lista = ValoresPorAsignacion()
print(f"Ordenado de menor a mayor: {OrdenamientoMayor(lista)} ")
print(f"Ordenado de mayor a menor {OrdenamientoMenor(lista)}")

