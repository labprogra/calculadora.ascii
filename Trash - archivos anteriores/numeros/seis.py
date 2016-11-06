#seis
matriz = []
for i in range(7):
    matriz.append([])
    for j in range(5):
        if (i==0 or i==3 or i==6 or j==0):
            matriz[i].append("x")
        elif (i>3 and j==4):
            matriz[i].append("x")
        else: matriz[i].append(".")
for i in matriz:
    print(i)
