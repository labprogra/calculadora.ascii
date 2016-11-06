#signo mas
matriz = []
for i in range(7):
    matriz.append([])
    for j in range(5):
        if i==3 :
            matriz[i].append("x")
        elif (i>0 and i<6) and j==2:
            matriz[i].append("x")   
        else: matriz[i].append(".")
for i in matriz:
    print(i)
