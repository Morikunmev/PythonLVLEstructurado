def CargaLista():
    lista = []
    for i in range(5):
        valor = int(input("Ingrese valor: "))
        lista.append(valor)
    return lista
def RetornarMayorMenor(n):
    mayor = n[0]
    menor = n[0]
    for i in range(1,len(n)):
        if n[i]>mayor:
            mayor = n[i]
        elif n[i]<menor:
            menor = n[i]
    return [menor,mayor]

lista = CargaLista()
rango = RetornarMayorMenor(lista)
print("El menor elementos de la lista es: ",rango[0])
print("El mayor elemento de la lista es: ",rango[1])

