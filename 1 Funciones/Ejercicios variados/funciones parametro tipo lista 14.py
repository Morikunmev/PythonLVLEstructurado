def MultiplicarLista(n):
    productor = 1
    for i in range(len(n)):
        productor*=n[i]
    return productor
def ContarPares(n):
    cont = 0
    for i in range(len(n)):
        if n[i] % 2 == 0:
            cont+=1
    return cont
def Promediodef(n):
    suma = 0
    for i in range(len(n)):
        suma+=n[i]
    promedio = suma / len(n)
    return promedio
def Primo(n):
    if n <2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True
def EncontrarPrimero(n):
    cant = 0
    for i in range(len(n)):
        if Primo(n[i]):
            cant+=1
    return cant
def EliminarDuplicados(n):
    i = 0
    for i in n:
        if i in n:
            i+=1
    return i




lista = [13,1313,412,3,1,2,2,2,2,2,2,2,2,22,2,2,2,3]
print(lista)
print("El producto es: ",MultiplicarLista(lista))
print("El total de numeros pares es: ",ContarPares(lista))
print(f"El promedio es: {Promediodef(lista)}")
print(f"Cantidad de numeros primos: {EncontrarPrimero(lista)}")
print(f"Cantidad de duplicados: {EliminarDuplicados(lista)}")

