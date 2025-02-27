def sumadef(*n):
    suma = 0
    for i,valor in enumerate(n):
        suma+=valor
    return suma

print(sumadef(2,3,3,3,3,3,3))
print(sumadef(*[2,3,3,3,3,3]))
print(sumadef(*(2,3,3,3,3,3,3)))

#Cantida fija de variables
def sumadef1(n1,n2,n3):
    return n1 + n2 + n3
print(sumadef1(*[2,2,2]))