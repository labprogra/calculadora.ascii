matriz = []
for i in range(7):
    matriz.append([])
    for j in range(5):
        if (j == 4 or i==0):
            matriz[i].append("x")
        else:
            matriz[i].append(".")

for i in matriz:
    print(i)
