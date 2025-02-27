diccionario = {"numero1":1,"numero2":15,"numero3":12}
for clave, valor in diccionario.items():
    if valor<10:
        diccionario[clave]=0
print(diccionario)
del diccionario["numero1"]
print(diccionario)