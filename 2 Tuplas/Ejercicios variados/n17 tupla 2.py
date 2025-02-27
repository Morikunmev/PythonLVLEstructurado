def RegistroLibros():
    registro = (("Cien años de soledad","Gabriel",1967),
                ("1984","George Orwell",1949),("Don Quijote","Miguel",1616),
                ("Matar a un ruiseñor","Harper",1960),("El gran gatsby","Scott",1925))
    return registro
def RegistroUsuarios():
    registro = (("jsmith","password123"),("mjones","securepass"),("igonsalez","123abcd"),("asanchez","mysecret"),
                ("rwilliams","python2023"),("richard","1234"))
    return registro
def Logindef():
    registro = RegistroUsuarios()
    intento = 0
    intento1 = 0
    while intento<3:
        usuario = input(f"Ingrese su usuario {intento+1} / 3: ")
        contraseña = input(f"Ingrese su contraseña {intento+1} / 3: ")
        for i in registro:
            if usuario in i[0] and contraseña in i[1]:
                print("Bien")
                intento = 2
                opcion = int(input("Elige la opcion a hacer\n "
                            "1.Consultar Libros \n "
                            "R: "))
                if opcion == 1:
                    while intento1 < 3:
                        consulta = input("Elige el libro a consultar: ")
                        for i in RegistroLibros():
                            if i[0] == consulta:
                                print(i)
                                break
                        else:
                            intento1+=1
                else:
                    break
        else:
            intento+=1
Logindef()