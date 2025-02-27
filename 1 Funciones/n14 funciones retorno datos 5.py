def retornar_perimetro(lado):
    perimetro = lado * 4
    return perimetro

lado = int(input("Ingrese el lado de un cuadrado: "))
print(f"El perimetro del cuadrado es: ",retornar_perimetro(lado))