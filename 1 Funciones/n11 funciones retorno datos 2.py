def retornar_mayor(v1,v2):
    if v1>v2:
        mayor = v1
    else:
        mayor = v2
    return mayor

valor1 = int(input("Ingrese primer valor: "))
valor2 = int(input("Ingrese segundo valor: "))
print(retornar_mayor(valor1,valor2))

# otra forma

def retornar_mayor(v1,v2):
    if v1>v2:
        return v1
    else:
        return v2
valor1 = int(input("Ingrese primer valor: "))
valor2 = int(input("Ingrese segundo valor: "))
x = retornar_mayor(valor1,valor2)
print(x)