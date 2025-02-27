def CargarLista():
    lista = []
    for i in range(5):
        i = i+1
        valor = int(input(f"Ingresa {i}/{5}: "))
        lista.append(valor)
    return lista
def MayorLista(n):
    mayor = 0
    menor = n[0]
    for i in range(len(n)):
        if n[i]>mayor:
            mayor = n[i]
        elif n[i]<menor:
            menor = n[i]
    return menor,mayor


lista = CargarLista()
menor, mayor = MayorLista(lista)
print(f"El menor de la lista es {menor}")
print(f"El mayor de la lista es {mayor}")
