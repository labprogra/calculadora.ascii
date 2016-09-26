
#el numero uno en matriz de 7x5


#uno
matriz = []
for i in range(7):
    matriz.append([])
    for j in range(5):
        if (j == 4):
            matriz[i].append("x")
        else:
            matriz[i].append(".")

for i in matriz:
    print(i)
