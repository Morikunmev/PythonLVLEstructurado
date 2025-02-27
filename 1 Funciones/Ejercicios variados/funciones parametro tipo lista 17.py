def mayormenor(n):
    mayor = 0
    menor = n[0]
    for i in n:
        if i>mayor:
            mayor = i
        elif i<menor:
            menor = i
    print("El valor menor es: ",menor)
    print("El valor mayor es: ",mayor)




listax = []
final = 4
for i in range(final):
    valor = int(input("Ingrese: "))
    listax.append(valor)
mayormenor(listax)