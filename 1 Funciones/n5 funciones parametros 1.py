def mensaje(mensaje):
    print("-"*20)
    print(mensaje)
    print("-"*20)
def carga_suma():
    acumulador = 0
    valor1 = int(input("Ingrese primer valor: "))
    acumulador+=1
    valor2 = int(input("Ingrese segundo valor: "))
    acumulador+=1
    print(f"La suma de los {acumulador} valores es {valor1+valor2}")

mensaje("El programa calcula la suma de dos valores ingresados")
carga_suma()
mensaje("Programa finalizado")