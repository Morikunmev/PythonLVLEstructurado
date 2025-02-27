def mayordef(n):
    mayor = ""
    menor = n[0]
    for i in range(len(n)):
        if len(n[i])>len(mayor):
            mayor = n[i]
        elif len(n[i])<len(menor):
            menor = n[i]
    print(f"Palabra con mas caracteres es: {mayor}")
    print(f"Palabra con menos caracteres es: {menor}")

palabras = ["enero","febrero","marzo","abril","mayo","junio"]
mayordef(palabras)