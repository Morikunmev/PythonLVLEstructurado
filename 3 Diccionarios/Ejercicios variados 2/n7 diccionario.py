def Numerosdef():
    numeros = {"numero1":(23,45),"numero2":(14,2332),"numero3":(17,433),"numero4":(15,45),"numero5":(10,3423)}
    return numeros

def Imprimir(numeros):
    for i, (clave, (valor1, valor2)) in enumerate (numeros.items()):
        print(i, clave,valor1,valor2)
def Sumarizar(numeros):
    suma = 0
    for i, (clave, (valor1, valor2)) in enumerate(numeros.items()):
        suma+=valor1+valor2
    return suma

numeros = Numerosdef()
Imprimir(numeros)
print(Sumarizar(numeros))