def tabla(numero, terminos = 10):
    for i in range(terminos):
        print(i*numero,",",sep="    ",end="")
    print()

tabla(3)
tabla(3,5)
tabla(terminos=20,numero=3)
