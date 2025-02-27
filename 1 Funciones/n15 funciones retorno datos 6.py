def retornar_superficie(lado1, lado2):
    superficie = lado1 * lado2
    return superficie

print("Primer rectangulo")
lado1 = int(input("Ingrese lado menor del rectangulo: "))
lado2 =int(input("Ingrese lado mayor del rectangulo: "))
print("Segundo rectangulo")
lado3 = int(input("Ingrese lado menor del rectangulo: "))
lado4 = int(input("Ingrese lado mayor del rectangulo: "))

area1 = retornar_superficie(lado1, lado2)
area2 = retornar_superficie(lado3, lado4)

if area1 == area2:
    print("Tienen la misma superficie")
elif area1>area2:
    print(f"El area 1 tiene mayor superficie que es: {area1}")
elif area1<area2:
    print(f"El area 2 tiene mayor superficie que es: {area2}")









