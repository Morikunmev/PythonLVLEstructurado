def MensajeMayordef():
    print("El mayor es: ")
def MensajeMenordef():
    print("El menor es: ")

def EncontrarMayor(n1,n2,n3):
    if n1>n2 and n1>n3:
        print(n1)
    elif n2>n1 and n2>n3:
        print(n2)
    else:
        print(n3)
def EncontrarMenor(n1,n2,n3):
    if n1<n2 and n1<n3:
        print(n1)
    elif n2<n1 and n2<n3:
        print(n2)
    else:
        print(n3)


def Cargar(mensaje):
    print(mensaje)
    n1 = int(input("Ingrese: "))
    n2 = int(input("Ingrese: "))
    n3 = int(input("Ingrese: "))
    MensajeMayordef()
    EncontrarMayor(n1,n2,n3)
    MensajeMenordef()
    EncontrarMenor(n1,n2,n3)

Cargar("Bienvenido al programa")
