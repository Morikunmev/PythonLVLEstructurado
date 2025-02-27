def producto(lista):
    prod = 1
    for x in range(len(lista)):
        prod*=lista[x]
    return prod

lista = [1,2,3,4,5]
print(lista)
print("Multiplicacion de todos sus elementos: ",producto(lista))
