def CargaNumeros():
    lista = []
    for i in range(5):
        lista.append(int(input(f"Ingrese valor {i+1}: ")))
    return lista
def ConversionTupla(numero):
    return tuple(numero)
def MayorMenor(n):
    mayor = 0
    menor = n[0]
    for i, valor in enumerate(n):
        if valor>mayor:
            mayor = valor
        elif valor<menor:
            menor = valor
    return (mayor, menor)

numero1 = CargaNumeros()
numero1 = ConversionTupla(numero1)
mayor, menor = MayorMenor(numero1)
print(f"El mayor es {mayor}")
print(f"El menor es {menor}")
mayormenor = MayorMenor(numero1)
print(f"El mayor es {mayormenor[0]}")
print(f"El menor es {mayormenor[1]}")
