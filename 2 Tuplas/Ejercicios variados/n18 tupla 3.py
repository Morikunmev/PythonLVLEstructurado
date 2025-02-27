def Registro():
    usuarios = (("user1","password"),("pythoncoder","secretpython"),("testaccount","12345test"),
                ("devguy23","codinglsfun"),("studentx","learningpython"),("demouser","987demo"),("richard","1234"))
    return usuarios
def RegistroPeliculas():
    Peliculas = (("el padrino","Francis","Crimen"),("pulp fiction","Quientin","Crimen"),("titanic","james","drama"),
                 ("el señor de los anillos","peter","fantasia"),("forest gump","robert","comedia"))
    return Peliculas
def AñadirPeliculas(n):
    n = list(n)
    titulo = input("Añadir titulo: ")
    director = input("Añadir director: ")
    genero = input("Añadir genero: ")
    comprimido = (titulo,director,genero)
    n.append(comprimido)
    return tuple(n)

def AñadirUsuarios(registro):
    registro = list(registro)
    usuario = input("Ingrese usuario: ")
    contraseña = input("Ingrese contraseña: ")
    comprimido = (usuario,contraseña)
    registro.append(comprimido)
    return tuple(registro)
def Login():
    i = 0
    while i<3:
        usuario = input(f"Ingrese su usuario {i+1} / 3: ")
        contraseña = input(f"Ingrese su contraseña {i+1} / 3: ")

        for x in Registro():
            if usuario == x[0] and contraseña == x[1]:
                i = 2
                print("Registrado Exitoso")
                opcion = int(input("Eliga la opcion a realizar: \n"
                               "1. Consulta de Peliculas \n"
                               "2. Añadir Peliculas \n"
                               "3. Consultar Usuarios \n"
                               "4. Añadir Usuarios \n"
                               "R: "))
                if opcion == 1:
                    consulta = input("Ingrese la pelicula a consultar: ")
                    for g in RegistroPeliculas():
                        if g[0] in consulta:
                            print(g)
                            break
                elif opcion == 2:
                    print(AñadirPeliculas(RegistroPeliculas()))
                    break
                elif opcion == 3:
                    consulta = input("Ingrese el usuario a consultar: ")
                    for g in Registro():
                        if consulta in g[0]:
                            print(g)
                            break
                elif opcion == 4:
                    print(AñadirUsuarios(Registro()))
                    break
                else:
                    i = 2
        else:
            i+=1
Login()