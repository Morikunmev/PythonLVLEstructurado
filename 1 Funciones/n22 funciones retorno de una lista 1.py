def carga_lista():
    li = []
    for i in range(5):
        valor = int(input("Ingrese valor: "))
        li.append(valor)
    return li
def imprimir_mayores10(li):
    print("Elementos de la lista mayores a 10")
    for i in range(len(li)):
        if li[i]>10:
            print(li[i])

lista = carga_lista()
imprimir_mayores10(lista)