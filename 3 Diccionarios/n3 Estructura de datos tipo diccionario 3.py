def Carga():
    diccionario = {}
    continua = "s"
    while continua == "s":
        ingles = input("Ingrese la palabra en ingles: ")
        castellano = input("Ingrese la palabra en castellano ")
        diccionario[ingles]=castellano
        continua = input("Quiere cargar otra palabra [s/n]")
    return diccionario
def Imprimir(diccionario):
    print("Listado completo del diccionario")
    for indice in diccionario:
        print(indice, diccionario[indice])
def ConsultaPalabra(diccionario):
    pal = input("Ingrese la palabra en ingles a consultar:")
    if pal in diccionario:
        print("En castellano significa",diccionario[pal])
    else:
        print("No esta la traduccion de dicha palabra")
diccionario = Carga()
Imprimir(diccionario)
ConsultaPalabra(diccionario)