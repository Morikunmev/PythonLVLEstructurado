def Cargar():
    lista = []
    for i in range(5):
        pais = input("Ingrese pais: ")
        cantidad = int(input("Ingrese habitantes: "))
        comprimido = (pais,cantidad)
        lista.append(comprimido)
    return lista
def Imprimir(n):
    for i in n:
        print(i)
def MayorMenor(n):
    mayor = n[0][1]
    nombremayor = n[0][0]
    menor = n[0][1]
    nombremenor = n[0][0]
    for i in n:
        if i[1]>mayor:
            mayor = i[1]
            nombremayor = i[0]
        elif i[1]<menor:
            menor = i[1]
            nombremenor = i[0]
    return (mayor,nombremayor,menor,nombremenor)

lista = Cargar()
Imprimir(lista)
mayormenor = MayorMenor(lista)
print(f"La mayor cantidad de habitantes es del pais {mayormenor[1]} que son {mayormenor[0]}")
print(f"La menor cantidad de habitantes es del pais {mayormenor[3]} que son {mayormenor[2]}")
