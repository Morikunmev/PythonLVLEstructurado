def Poblacionesdef():
    poblacion = {"india":1436510000,"china":1411961000,"eeuu":335537000,
                 "indonesia": 277432000,"pakistan":231552000}
    return poblacion
def Imprimir(paises):
    for clave, valor in paises.items():
        print(clave,valor)
def MaximoPoblacion(paises):
    maximo = 0
    nombremaximo = ""
    diccionario = {}
    for clave, valor in paises.items():
        if valor>maximo:
            maximo = valor
            nombremaximo = clave
    diccionario[nombremaximo]=maximo
    return diccionario
paises = Poblacionesdef()
Imprimir(paises)
print(f"Pais con mas poblacion es: \n {MaximoPoblacion(paises)}")