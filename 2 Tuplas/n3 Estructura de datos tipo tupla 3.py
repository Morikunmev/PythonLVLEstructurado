fechatupla1 = (1,5,2020)
print("Imrprimir la tupla")
print(fechatupla1)
fechatupla1 = list(fechatupla1)
print("Imprimimos la lista que se copip de la tupla")
print(fechatupla1)
fechatupla1[0]=25
print("Imprimimos la lista modificada")
print(fechatupla1)

fechatupla2 = tuple(fechatupla1)
print("Imprimimos la segunda tupla que se le copio la lista")
print(fechatupla2)

dia = 10
mes = 5
año = 2020
#Empaquetar
fechatupla3 = dia,mes, año
#Desempaquetar
dia1, mes1, año1 = fechatupla3
dia1 = 30
mes1 = 12
año1 = 1998
fechatupla3 = dia1,mes1,año1
print(fechatupla3)