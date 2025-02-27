def Promediodef(n):
    return round(n / final,4)

final = 3
ac= 0
for i in range(final):
    valor = int(input("Ingrese: "))
    ac+=valor
print("El promedio es: ",Promediodef(ac))

