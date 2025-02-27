def CargaValores():
    tupla = []
    for i in range(5):
        valor = int(input(f"Ingrese {i+1}/{5}: "))
        tupla.append(valor)
    tupla = tuple(tupla)
    return tupla
def desempaquetado(*n):
    return (n[0] + n[1] + n[2] + n[3] + n[4])
def desempaquetado1(n1,n2,n3,n4,n5):
    return n1 + n2 + n3 + n4 + n5

tupla = CargaValores()
#Desempaquetado
v1, v2,v3,v4,v5 = tupla
#Valores nuevos
v1, v2, v3, v4, v5 = 12,15,16,17,15
#Empaquetado
tupla = v1,v2,v3,v4,v5
print(tupla)
NuevaTupla = desempaquetado1(*tupla)
print(NuevaTupla)
