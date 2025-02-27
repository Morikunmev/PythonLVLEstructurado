#empaquetado en bloque principal

dia = 30
mes = 12
año = 1998
fecha1= dia, mes, año
#desempaquetado
dia1, mes1, año1 = fecha1
dia1 = 15
mes1 = 11
año1 = 1955
print(dia1,mes1,año1)

#desempaquetado dentro de una funcion
def empaquetado1(*n1):
    return n1[0] + n1[1] + n1[2]
suma = [2,3,5,4,4]
print(empaquetado1(*suma))

def empaquetado2(n1,n2,n3):
    return n1 + n2 + n3
suma1 = [2,3,3,3,3,3]
print(empaquetado1(*suma1))
