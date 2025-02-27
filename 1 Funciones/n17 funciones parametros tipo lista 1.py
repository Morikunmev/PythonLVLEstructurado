def sumarizar(lista):
    suma = 0
    for i in range(len(lista)):
        suma+=lista[i]
    return suma
def mayordef(lista):
    mayor = 0
    for i in range(len(lista)):
        if lista[i]>mayor:
            mayor = lista[i]
    return mayor
def menordef(lista):
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i]<menor:
            menor = lista[i]
    return menor

listavalores = [10,20,30,40,50]
print("Lista Completo")
print(listavalores)
print("La suma de todos sus elementos",sumarizar(listavalores))
print("El mayor de los elementos es: ",mayordef(listavalores))
print("El menor de los elementos es: ",menordef(listavalores))
