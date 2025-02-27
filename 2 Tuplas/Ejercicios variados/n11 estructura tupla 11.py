def TresValores():
    n1 = 2
    n2 = 3
    n3 = 5
    return (n1,n2,n3)
def TresValores1(n1=4,n2=5,n3=6):
    return (n1,n2,n3)
def Imrpimir(n):
    print(f"El valor ingresado es {n}")

def Conversion1(n):
    n = list(n)
    return n
def Conversion2(n):
    n = tuple(n)
    return n

numero1 = TresValores()
Imrpimir(numero1)

numero2 = TresValores1(n2=2)
Imrpimir(numero2)

#Conversion a lista
numero1 = Conversion1(numero1)
numero2 = Conversion1(numero2)

print(numero1)
print(numero2)

#Conversion a tupla
numero1 = Conversion2(numero1)
numero2 = Conversion2(numero2)

#Empaquetamiento en el bloque principal
n1 = 45
n2 = 21
n3 = 12
numero3 = n1,n2,n3
#Desempaquetamiento en el bloque principal
n1,n2,n3 = numero3
#Cambio de valores en las variables desempaquetadas
n1,n2,n3 = 1231,12312,12312
numero3 = n1,n2,n3
print(numero3)
#Conversion de la tupla a tipo lista
numero3 = Conversion1(numero3)
#Cambio de valores por medio de los subindices en la lista
numero3[0] = 23
numero3[1] = 12
numero3[2] = 1
#Conversion de la lista a tipo tupla
numero3 = Conversion2(numero3)
print(numero3)

