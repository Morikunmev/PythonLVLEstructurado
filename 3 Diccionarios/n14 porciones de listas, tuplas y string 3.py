def PrimerosTres(cadena):
    return cadena[:3]
def mesesdef():
    meses =("enero","frebero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
    return meses
def Imprimirmes():
    for mes in mesesdef():
        print(PrimerosTres(mes))
Imprimirmes()