import random

def opcion():
    aleatorio=random.randint(1,100)
    intento=0
    elegido=0
    while elegido!=aleatorio:
        elegido=int(input("Cual numero elige?"))
        if aleatorio>elegido:
            print("Piense en un numero mayor")
        else:
            print("Piensa en un numero menor")
        intento+=1
    print(f"Ganaste con {intento} intentos")
numero =opcion()
