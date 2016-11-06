uno = []
for i in range(7):
	uno.append([])
	for j in range(5):
		if (j == 4):
			uno[i].append("x")
		else:
			uno[i].append(".")

#....x.xxxxx.xxxxx.x...x.xxxxx.xxxxx.xxxxx.......xxxxx.xxxxx.xxxxx
#....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x
#....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x
#....x.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.....x.xxxxx.xxxxx.xxxxx.x...x
#....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x
#....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x
#....x.xxxxx.xxxxx.....x.xxxxx.xxxxx.....x.......xxxxx.xxxxx.xxxxx

fila = ["....x.xxxxx.xxxxx.x...x.xxxxx.xxxxx.xxxxx.......xxxxx.xxxxx.xxxxx","....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x","....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x","....x.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.....x.xxxxx.xxxxx.xxxxx.x...x","....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x","....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x","....x.xxxxx.xxxxx.....x.xxxxx.xxxxx.....x.......xxxxx.xxxxx.xxxxx"]
numero = []
op = []
for i in range(7):
	numero.append([])
	numero[i] = list(fila[i])		#separa todos los caracteres de la fila
#for i in numero:
#	print (i)			#ejemplos, cada fila se transforma en una matriz de (i+1) elementos
#print ((numero[0])[4]) 	#fila 0 columna 4



for i in range(7):
	op.append([])
	for j in range(int(len(numero[i])/6)+1):
		op[i].append([])
		for k in range(5):
			op[i][j].append(numero[i][k+6*j])		#en cada columna se guarda un numero ASCII diferente
			
#num1=[op[0][0],op[1][0],op[2][0],op[3][0],op[4][0],op[5][0],op[6][0]]
#entero1=0
#if num1==uno:
#	entero1=1
#print (entero1)				#prueba muy ordinaria para asignar el numero


#print (op[6][0])	#ejemplo1
#print ()
#for i in op:		#ejemplo 2
#	print (i)




			