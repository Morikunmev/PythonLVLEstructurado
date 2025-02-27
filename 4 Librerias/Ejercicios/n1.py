import random
def condicional():
    if suma==25 or suma==20 or suma==15:
        print("Ganaste")
    else:
        print("Perdiste")
def mostrardef():
    print("Suma:",dado1)
    print("Suma:",dado2)
    print("Suma:",dado3)
    print("Suma:",dado4)
    print("Suma:",dado5)

def sumadef():
    suma = dado1 + dado2 + dado3 + dado4 + dado5
    return suma
dado1=random.randint(1,6)
dado2=random.randint(1,7)
dado3=random.randint(1,8)
dado4=random.randint(1,9)
dado5=random.randint(1,10)

mostrar=mostrardef()
suma=sumadef()
imprimir=condicional()

        
