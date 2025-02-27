def multiplicacion(lista,valor):
    for x in range(len(lista)):
        multi = lista[x] * valor
        print(multi)

lista = [3,7,8,2,10]
print("Lista original")
print(lista)
print("Lista de los elementos multiplicados por 3")
multiplicacion(lista,3)