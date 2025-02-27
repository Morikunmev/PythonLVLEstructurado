def cargar():
    lista = []
    for x in range(5):
        valor = int(input("Ingrese valor: "))
        lista.append(valor)
    return lista
def MayorMenor(n):
    mayor = 0
    menor = n[0]
    for x, valor in enumerate(n):
        if valor>mayor:
            mayor = valor
        elif valor<menor:
            menor = valor
    return (mayor, menor)
lista = cargar()
mayor, menor = MayorMenor()
print("El valor maximo es: ",mayor)
print("El valor minimo es: "menor)