
#print chr(33)
#33 equivale a un ! en caracteres

#print ord('!')
#! equivale a un 33 en caracteres


#crear una matriz de de 7 filas y 5 columnas


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


matriz = []
for i in range(7):
    matriz.append([])
    for j in range(5):
        matriz[i].append(".")

for i in matriz:
    print(i)
