def primer():
    final = 3
    numeros = []
    for i in range(final):
        valor= int(input(f"Ingrese un valor {i+1} de {final}"))
        numeros.append(valor)
    menor = numeros[0]
    for i in range(len(numeros)):
        if numeros[i]<menor:
            menor = numeros[i]
    print(f"El menor es: {menor}")

    mayor=numeros[i]
    for i in range(len(numeros)):
        if numeros[i]>mayor:
            mayor = numeros[i]
    print(f"El mayor es: {mayor}")


#Sin estructura for

def segundo():
    valor1 = int(input("Ingresa 1: "))
    valor2 = int(input("Ingresa 2: "))
    valor3 = int(input("Ingresa 3: "))

    if valor1 > valor2 and valor1 >valor3:
        print(f"El mayor es: {valor1}")
    elif valor2>valor1 and valor2 >valor3:
        print(f"El mayor es: {valor2}")
    else:
        print(f"El mayor es: {valor3}")
    if valor1 <valor2 and valor1 <valor3:
        print(f"El menor valor es: {valor1}")
    elif valor2 < valor1 and valor2 < valor3:
        print(F"El menor valor es: {valor2}")
    else:
        print(f"El menor valor es: {valor3}")

segundo()