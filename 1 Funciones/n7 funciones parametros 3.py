def MensajeDef(mensaje):
    valor = int(input(mensaje))
    Imprimir(valor)
    desiciondef(valor)

def Imprimir(n1):
    print(f"Lado ingresado: {n1}")
def calculo1(n1):
    print(f"El area es {n1*n1}")
def calculo2(n1):
    print(f"El perimetro es {n1+n1+n1+n1}")

def desiciondef(valor):
    opcion = int(input("Calcular Area (1) o Perimetro (2)?: "))
    if opcion == 1:
        calculo1(valor)
    elif opcion == 2:
        calculo2(valor)

MensajeDef("Ingresa el lado de un cuadrado: ")