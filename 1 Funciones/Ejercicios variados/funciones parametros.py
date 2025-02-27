def cargar():
    final = 3
    mayor = 0
    menor = 10000000
    for i in range(final):
        valor = int(input(f"Ingrese un valor de {i+1}/{final}: "))
        if valor>mayor:
            mayor = valor
        if valor<menor:
            menor = valor
    mensajedef(f"El mayor valor es: {mayor}")
    mensajedef(f"El menor valor es: {menor}")

def mensajedef(mensaje):
    print(mensaje)
cargar()