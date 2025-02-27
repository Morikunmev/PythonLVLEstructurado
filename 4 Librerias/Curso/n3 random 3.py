import random

print("Intente adivinar el numero que pense entre 1 y 100")
aleatorio=random.randint(1,100)
intentos=0
elegido=0
while elegido!=aleatorio:
    elegido=int(input("Cual numero elige?: "))
    if aleatorio>elegido:
        print("Pense un numero mayor")
    elif aleatorio<elegido:
        print("Pense un numero menor")
    intentos=intentos+1
print("Ganaste en",intentos,"intentos")
