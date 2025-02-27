def Carga():
    lista = []
    for i in range(5):
        valor = int(input("Ingresa: "))
        lista.append(valor)
    return lista
def Imprimir(numeros):
    for i in numeros:
        print(i)
def mayordef(numeros):
    mayor = numeros[0]
    for i in numeros:
        if i>mayor:
            mayor = i
    return mayor
def Sumadef(numeros):
    suma = 0
    for i in numeros:
        suma+=i
    return suma
numeros = Carga()
mayor = mayordef(numeros)
suma = Sumadef(numeros)
print(f"El mayor es: {mayor}")
print(f"La suma de todos los elementos es {suma}")