def Imprimir(paises):
    for clave in paises:
        print(clave,paises[clave])

paises = {"argentina": 400000,"españa":450000,"brasil":1999999,"uruguay":340000}
Imprimir(paises)