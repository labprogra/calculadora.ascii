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
caracter = []
numero = []
for i in range(7):
	caracter.append([])
	caracter[i] = list(fila[i])
#for i in caracter:
#	print (i)			#ejemplos, cada fila se transforma en una matriz de (i+1) elementos
#print ((caracter[0])[4]) 	#fila 0 columna 4



for i in range(7):
	numero.append([])
	for j in range(int(len(caracter[i])/6)+1):
		numero[i].append([])
		for k in range(5):
			numero[i][j].append(caracter[i][k+6*j])		#en cada columna se guarda un numero ASCII diferente
			
#num1=[numero[0][0],numero[1][0],numero[2][0],numero[3][0],numero[4][0],numero[5][0],numero[6][0]]
#entero1=0
#if num1==uno:
#	entero1=1
#print (entero1)				#prueba muy ordinaria


#print (numero[6][0])	#ejemplo1
#print ()
#for i in numero:		#ejemplo 2
#	print (i)

#for i in range(7):
#	print (numero[i][0]) #numero_ij		#otra prueba


			