def Imprimir(n):
    for i in n:
        print(i[0], i[1], i[2])
def MayorMenor(n):
    mayor = n[0][1]
    menor = n[0][1]
    for i in n:
        if i[1]>mayor:
            mayor = i[1]
        elif i[1]<menor:
            menor = i[1]
    return (mayor,menor)