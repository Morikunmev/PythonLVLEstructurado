def Numerosdef():
    numeros = {"numero1":[23,34],
               "numero2":[14,35],
               "numero3":[17,34],
               "numero4":[15,12],
               "numero5":[10,23]}
    return numeros
def Imprimir(numeros):
    for i, (clave, [valor1, valor2]) in enumerate (numeros.items()):
        print(f"registro nro {i+1}: {clave}, {valor1}{valor2}")
numeros = Numerosdef()
Imprimir(numeros)
