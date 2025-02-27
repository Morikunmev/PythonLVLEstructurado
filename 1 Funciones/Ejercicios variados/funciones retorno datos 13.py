def string(mensaje):
    n = input(mensaje)
    n = n.count("a") + n.count("e") + n.count("i") + n.count("o") + n.count("u")
    return n


print(string("Ingrese caracter: "))