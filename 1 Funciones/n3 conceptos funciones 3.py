def primero():
    valor = int(input("Ingresa un numero entero: "))
    print(f"El {valor} al cuadrado es {pow(valor,2)}")
          
def segundo():
    acumulador = 1
    final = 7
    for i in range(final):
        valor=int(input(f"Ingresa un valor {i+1} de {final}: "))
        acumulador*=valor
    print(f"El valor de los {final} numeros es: {acumulador}")

primero()
segundo()