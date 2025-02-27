def OrdenamientoMayor(n):
    for i in range(len(n)-1):
        for x in range((len(n)-1)-i):
            if n[x]>n[x+1]:
                n[x], n[x+1] = n[x+1],n[x]
    print("Ordenados de mayor a menor")
    print(n)
def OrdenamientoMenor(n):
    for i in range(len(n)-1):
        for x in range((len(n)-1)-i):
            if n[x]<n[x+1]:
                n[x],n[x+1] = n[x+1],n[x]
    print("Ordenados de menor a mayor")
    print(n)

def Cargar(mensaje):
    lista = []
    final = 4
    for i in range(final):
        valor = int(input(f"{mensaje} {i+1} de {final}: "))
        lista.append(valor)
    print("valores agregados")
    print(lista)
    OrdenamientoMayor(lista)
    OrdenamientoMenor(lista)

Cargar(f"Ingresa valor")
