def PaisesFriosdef():
    ciudades = {"Rusia": ("Yakutsk",-10.4),
                "Rusia": ("Dudinka",-13.2),
                "China": ("Habin",1.4),
                "Canada": ("Yellowknife",-10.0)}
    return ciudades

def Maximo(PaisesFrios):
    maximo = None
    ciudadalta = None
    maxpais = None
    for pais, (ciudad,temp) in PaisesFrios.items():
        if maximo is None or temp >maximo:
            maximo = temp
            ciudadalta = ciudad
            maxpais = pais
    print(f"La ciudad con mas temperatura es {ciudadalta} con {maximo} temperatura del pais {maxpais}")


def Minimo(PaisesFrios):
    minimo = None
    ciudadbaja = None
    minpais = None
    for pais, (ciudad, temp) in PaisesFrios.items():
        if minimo is None or temp<minimo:
            minimo = temp
            ciudadbaja = ciudad
            minpais = pais
    print(f"La ciudad con menos temeperatura es {ciudadbaja} con {minimo} temperatura del pais {minpais}")


PaisesFrios = PaisesFriosdef()
Maximo(PaisesFrios)
Minimo(PaisesFrios)
