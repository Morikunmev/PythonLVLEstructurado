def frutasdef():
    frutas = {"manzana": 1.25,"platano":0.75,"naraja":0.90,"fresa":1.80,"kiwi":1.95}
    return frutas
def sumadef(frutas):
    suma = 0
    for clave, valor in frutas.items():
        suma+=valor
    return suma
def Consultadef(consulta,frutas):
        if consulta in frutas:
            print(frutas[consulta])

frutas = frutasdef()
Total = sumadef(frutas)
print("El total de las frutas es:",Total)
Consultadef("manzana",frutas)