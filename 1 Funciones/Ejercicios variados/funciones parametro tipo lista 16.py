def Mayordef(n):
    mayor = 0
    for i in n:
        if i>mayor:
            mayor = i
    return mayor
def Menordef(n):
    menor = n[0]
    for i in n:
        if i<menor:
            menor = i
    return menor


listax = []
final = 5
for i in range(final):
    i = i+1
    valor = int(input(f"Ingrese numero {i} / {final}: "))
    listax.append(valor)
print(f"El menor es {Menordef(listax)}")
print(f"El mayor es {Mayordef(listax)}")
