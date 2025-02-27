lista = {"numero":1,"sajasdjasdj":2}
print(lista["numero"])
for i in lista:
    print(i,lista[i])

lista1 = [13,1,321,13,132,132]
for x in lista1:
    if x == 1:
        lista1[x] = 0
print(lista1)