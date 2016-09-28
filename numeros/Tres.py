#tres
matriz = []
for i in range(7):
    matriz.append([])
    for j in range(5):
        if (j==4):
            matriz[i].append("x")
        elif((i==0 or i==6 or i==3) and (j==0 or j==1 or j==2 or j==3)):
              matriz[i].append("x")
        else: matriz[i].append(".")
for i in matriz:
    print(i)
