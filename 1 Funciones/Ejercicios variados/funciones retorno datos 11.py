def Perimetrodef(n):
    return n+n+n+n
def Principal(mensaje):
    valor = int(input(mensaje))
    perimetro = Perimetrodef(valor)
    print(f"El perimetro del cuadrado de lado {valor} es {perimetro}")

Principal("Ingrese el perimetro del cuadrado: ")