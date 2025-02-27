def empaquetar(*n):
    return n[0] + n[1] + n[2]

lista = [2,4,4,3]
lista1 = empaquetar(*lista)
print(lista1)