def cargar():
    lista=[]
    for i in range(5):
        valor=int(input("Ingrese un valor: "))
        lista.append(valor)
    return lista
def imprimir_mayor(lista):
    mayor=lista[0]
    for i in range(1,5):
        if lista[i]>mayor:
            mayor=lista[i]
    print("Mayor elemento de la lista:",mayor)
def imprimir_suma(lista):
    suma=0
    for i in lista:
        suma+=i
    print("La suma de sus elementos es: ",suma)
