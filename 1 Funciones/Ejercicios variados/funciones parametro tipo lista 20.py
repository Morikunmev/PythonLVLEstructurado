def productos(n):
    prod = 1
    for i in range(len(n)):
        prod*=n[i]
    return prod


lista = [2,3,54,5,4,343,1]
print(productos(lista))