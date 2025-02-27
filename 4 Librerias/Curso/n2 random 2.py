import random

def cargar():
    lista=[]
    for x in range(10):
        lista.append(random.randint(0,1000))
    return lista

def imprimir():
    print(lista)
    
def mezclar():
    random.shuffle(lista)
    
lista=cargar()
imprimir()
mezclar()
imprimir()
