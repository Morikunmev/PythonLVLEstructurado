def suma(v1,v2,v3 = 0,v4 = 0,v5 = 0):
    a = v1 + v2 + v3 + v4 + v5
    return a

print("La suma de 5 + 6: ",suma(5,6))
print("La suma de 5 + 6 + 3 = ",suma(5,6,3))
print("La suma de 1 + 1 +1 +1 = ",suma(1,1,1,1))
print(f"La suma de 1+1+1+1+1 = ",suma(1,1,1,1,1))
