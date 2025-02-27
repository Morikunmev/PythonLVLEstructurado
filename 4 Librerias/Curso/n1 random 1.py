import random

dado1=random.randint(1,6)
dado2=random.randint(1,6)
print("Primer dado:",dado1)
print("Segundo dato:",dado2)
suma=dado1+dado2
if suma==7:
    print("Gano")
else:
    print("Perdio")

#Para poder usar funcionalidades de la biblioteca estandar, tenemos que importar El modulo desde donde se encuentra

