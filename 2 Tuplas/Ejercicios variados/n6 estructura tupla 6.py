def empacar_lista(*args):
    return args

mi_lista = [1, 2, 3, 4]
mi_lista_empacada = empacar_lista(*mi_lista)
print(mi_lista_empacada)