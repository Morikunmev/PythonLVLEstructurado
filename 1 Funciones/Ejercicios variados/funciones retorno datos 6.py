def stringdef(mensaje):
    valor = input(mensaje)
    valor = len(valor)
    return valor
largo = stringdef("Ingresa un string: ")
print(f"El largo de los caracteres son: {largo}")


nombre1 = input("Ingrese un nombre: ")
nombre2 = input("Ingrese otro nombre: ")
if len(nombre1)>len(nombre2):
    print(f"f{nombre1} es el nombre mas largo")
else:
    print(f"{nombre2} es el nombre mas largo")