
def Principal(mensaje):
    final = 5
    mayor = 0
    menor = 100000
    for i in range(final):
        valor = int(input(mensaje))
        if valor >mayor:
            mayor = valor
        if valor<menor:
            menor = valor
    print(f"El mayor es: {mayor}")
    print(f"El menor es: {menor}")
Principal("Ingrese: ")