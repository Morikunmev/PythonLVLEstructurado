import random

def sumadef():
    suma=0
    for i in range(10):
        valor=random.randint(1,100)
        suma+=valor
    return suma
def restadef():
    resta=0
    for i in range(10):
        valor=random.randint(1,100)
        resta-=valor
    return resta
def imprimir():
    print("Producto")

suma=sumadef()
print(suma)
resta=restadef()
print(resta)
imprimir()
producto = suma * resta
print(producto)
    
