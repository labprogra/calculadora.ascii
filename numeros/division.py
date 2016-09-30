#signo division
matriz = []
for i in range(7):
    matriz.append([])
    for j in range(5):
        if (5-i)==j :
            matriz[i].append("x")  
        else: matriz[i].append(".")
for i in matriz:
    print(i)
