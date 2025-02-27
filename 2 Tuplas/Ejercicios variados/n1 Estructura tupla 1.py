def Imprimir(a,b,*n):
    suma = a + b
    for i,valor in enumerate(n):
        suma+=valor
    print(suma)


Imprimir(2,4,1,2,3,4,5,6)