import random

def cargar():
    lista=[]
    for i in range(4):
        lista.append(random.randint(1,3))
    lista.append(1)
    return lista

def controlar_primero():
    while lista[0]!=1:
        random.shuffle(lista)
def imprimir():
    print(lista)



#Bloque principal
lista=cargar()
imprimir()
controlar_primero()
imprimir()
