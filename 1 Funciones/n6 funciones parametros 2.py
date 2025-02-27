def MostrarValores(n1,n2,n3):
    print("El mayor de los 3 numeros es: ")
    if n1>n2 and n1>n3:
        print(n1)
    elif n2>n1 and n2>n3:
        print(n2)
    else:
        print(n3)
def Mensajedef():
    print("El menor de los 3 es: ")
def Menores(n1,n2,n3):
    Mensajedef()
    if n1<n2 and n1<n3:
        print(n1)
    elif n2<n1 and n2<n3:
        print(n2)
    else:
        print(n3)

def Cargar(Mensaje):
    print(Mensaje)
    valor1 = int(input("Ingrese un valor: "))
    valor2 = int(input("Ingrese un valor: "))
    valor3 = int(input("Ingrese un valor: "))
    MostrarValores(valor1,valor2,valor3)
    Menores(valor1,valor2,valor3)

Cargar("Bienvenio")

