def retornar_promedio(v1,v2,v3):
    promedio = (v1 + v2 + v3) / 3
    return promedio

valor1 = int(input("Ingrese primer valor: "))
valor2 = int(input("Ingrese segundo valor: "))
valor3 = int(input("Ingrese tercer valor: "))
print("El promedio de los 3 valores es: ",retornar_promedio(valor1,valor2,valor2))
