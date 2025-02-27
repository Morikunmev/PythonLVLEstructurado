def retornar_superficie(lado1,lado2):
    return lado1 * lado2
lista = []
mayor = 0
menor = 100000000000000000000000000000000000000000000000
for i in range(2):
    base = int(input("Ingrese la base del rectangulo: "))
    altura = int(input("Ingrese la altura del rectangulo: "))
    area = retornar_superficie(base,altura)
    print(f"Area: {area}")
    lista.append(area)
for i in range(len(lista)):
    if lista[i]>mayor:
        mayor = lista[i]
print(f"El lado mas grande encontrado es: {mayor}")

for i in lista:
    if i<menor:
        menor = i
print(f"El lado menor es: {menor}")
