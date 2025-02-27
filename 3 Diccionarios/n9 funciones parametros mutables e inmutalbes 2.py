def Cargar():
    nombre = []
    for x in range(5):
        nom = input("Nombre: ")
        nombre.append(nom)
    return nombre
def Ordenar(nombres):
    for k in range(4):
        for x in range(4):
            if nombres[x]>nombres[x+1]:
                aux = nombres[x+1]
                nombres[x]=nombres[x+1]
                nombres[x+1]=aux
def Imprimir(nombres):
    for nombre in nombres:
        print(nombre)
nombres = Cargar()
Imprimir(nombres)
Ordenar(nombres)
print("Ordenado")
Imprimir(nombres)