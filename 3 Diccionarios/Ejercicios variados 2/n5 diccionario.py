
def Numerosdef():
    numeros = {"numero1":23,"numero2":14,"numero3":17,"numero4":15,"numero5":10}
    return numeros
def Imprimir(numeros):
    for i, (clave, valor) in enumerate (numeros.items()):
        print(f"Registro {i+1}: {clave}:{valor}")
numeros = Numerosdef()
Imprimir(numeros)