def CalcularPerimetro(n1):
    print(f"El petrimetro es: {n1*4}")
def CalcularSuperficie(n1):
    print(f"La superficie es: {n1*n1}")

def cargar_lado(mensaje):
    valor = int(input(mensaje))
    opcion = int(input(f"Quieres calcular el perimetro (1) o el area? (2): "))
    if opcion == 1:
        CalcularPerimetro(valor)
    elif opcion == 2:
        CalcularSuperficie(valor)
cargar_lado("Ingrese un valor: ")