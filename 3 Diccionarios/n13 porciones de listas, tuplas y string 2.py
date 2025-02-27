def MesesFaltantes(numeros):
    meses =("enero","frebero","marzo","abril","mayo","junio","julio","agosto","septiembre","octubre","noviembre","diciembre")
    return meses[numeros:]
numeros = int(input("Ingrese el numero de mes: "))
mesesfalta = MesesFaltantes(numeros)
print(mesesfalta)