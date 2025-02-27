def sumar(v1,v2,*lista):
    suma = v1 + v2
    for i, valor in enumerate(lista):
        suma+=valor
    return suma
print(sumar(1,2))
print(sumar(1,2,3,4,5))
