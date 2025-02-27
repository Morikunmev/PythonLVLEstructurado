def cargar():
    lista = []
    for i in range(5):
        valor = int(input("Ingrese valor: "))
        lista.append(valor)
    return lista

def CalcularPromedio(n):
    suma = 0
    for i in range(len(n)):
        suma+=n[i]
    promedio = suma / len(n)
    return promedio
def ValorMayor(n):
    mayor = 0
    for i in n:
        if i>mayor:
            mayor = i
    return mayor



ListaValores = cargar()
promedio = CalcularPromedio(ListaValores)
print(f"El primedio es: {promedio}")
print(f"El mayor es: {ValorMayor(ListaValores)}")