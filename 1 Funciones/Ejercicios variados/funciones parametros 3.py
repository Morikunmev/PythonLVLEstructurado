def DefinirLargo(m):
    print(f"El largo es {len(m)}")
def CargarString(mensaje):
    evaluar = input(mensaje)
    DefinirLargo(evaluar)

for i in range(3):
    CargarString(f"Ingresa cualquier wea {i+1} /{3}: ")