def sumarizar(n):
    suma = 0
    for i in n:
        suma+=i
    return suma
def factorial(n):
    suma = 1
    for i in n:
        suma*=i
    return suma
listax=[]
final = 2
for i in range(final):
    i = i+1
    listax.append(i)

print("Lista sumarizada")
print(sumarizar(listax))

print(f"Lista factorial de: {final}")
print(factorial(listax))