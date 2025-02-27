def presentacion():
    print("programa que permite cargar por teclado dos valores")
    print("efectua la suma de los valores")
    print("muestra el resultado de la suma")
    print("-"*20)

def carga_suma():
    valor1 =int(input("Ingrese primer valor: "))
    valor2 =int(input("Ingrese segundo valor: "))
    suma = valor1 + valor2
    print(f"la suma de los 2 valores es: {suma}")
def finalizacion():
    print("Gracias por utilizar este programa")

presentacion()
carga_suma()
finalizacion()