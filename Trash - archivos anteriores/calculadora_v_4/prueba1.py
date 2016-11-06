#Acá se crean los números y operaciones ASCII
uno = []
for i in range(7):
	uno.append([])
	for j in range(5):
		if (j == 4):
			uno[i].append('x')
		else:
			uno[i].append('.')
dos = []
for i in range(7):
	dos.append([])
	for j in range(5):
		if (i==0 or i==3 or i==6):
			dos[i].append('x')
		elif (i<3 and j==4):
			dos[i].append('x')
		elif (i>3 and j==0):
			dos[i].append('x')
		else: dos[i].append('.')
tres = []
for i in range(7):
	tres.append([])
	for j in range(5):
		if (j==4):
			tres[i].append('x')
		elif((i==0 or i==6 or i==3) and (j==0 or j==1 or j==2 or j==3)):
			tres[i].append('x')
		else:
			tres[i].append('.')
cuatro = []
for i in range(7):
	cuatro.append([])
	for j in range(5):
		if (j==0 and i<4 or j==4):
			cuatro[i].append('x')
		elif((i<0 or i==3) and (j==1 or j==2 or j==3)):
			cuatro[i].append('x')
		else:
			cuatro[i].append('.')
cinco = []
for i in range(7):
	cinco.append([])
	for j in range(5):
		if (i==0 or i==3 or i==6):
			cinco[i].append('x')
		elif (i<3 and j==0):
			cinco[i].append('x')
		elif (i>3 and j==4):
			cinco[i].append('x')
		else: cinco[i].append('.')
seis = []
for i in range(7):
	seis.append([])
	for j in range(5):
		if (i==0 or i==3 or i==6 or j==0):
			seis[i].append('x')
		elif (i>3 and j==4):
			seis[i].append('x')
		else: seis[i].append('.')
siete = []
for i in range(7):
	siete.append([])
	for j in range(5):
		if (j == 4 or i==0):
			siete[i].append('x')
		else:
			siete[i].append('.')
ocho = []
for i in range(7):
	ocho.append([])
	for j in range(5):
		if (j==0 or j==4):
			ocho[i].append('x')
		elif((i==0 or i==6 or i==3) and (j==1 or j==2 or j==3)):
			ocho[i].append('x')
		else:
			ocho[i].append('.')
nueve = []
for i in range(7):
	nueve.append([])
	for j in range(5):
		if (j==4):
			nueve[i].append('x')
		elif((i==0 or i==6 or i==3) and (j==0 or j==1 or j==2 or j==3)):
			nueve[i].append('x')
		elif i<4 and j==0:
			nueve[i].append('x')
		else:
			nueve[i].append('.')
signomas = []
for i in range(7):
	signomas.append([])
	for j in range(5):
		if i==3 :
			signomas[i].append('x')
		elif (i>0 and i<6) and j==2:
			signomas[i].append('x')   
		else:
			signomas[i].append('.')
signomenos = []
multiplicacion = []
division = []
punto = []
indiceOperacion = 0
tipoOperacion = ''
numeroSt1 = ''
numeroSt2 = ''
numero1 = 0
numero2 = 0

#....x.xxxxx.xxxxx.x...x.xxxxx.xxxxx.xxxxx.......xxxxx.xxxxx.xxxxx
#....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x
#....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x
#....x.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.....x.xxxxx.xxxxx.xxxxx.x...x
#....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x
#....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x
#....x.xxxxx.xxxxx.....x.xxxxx.xxxxx.....x.......xxxxx.xxxxx.xxxxx

fila = ['....x.xxxxx.xxxxx.x...x.xxxxx.xxxxx.xxxxx.......xxxxx.xxxxx.xxxxx','....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x','....x.....x.....x.x...x.x.....x.........x...x...x...x.x...x.x...x','....x.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.....x.xxxxx.xxxxx.xxxxx.x...x','....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x','....x.x.........x.....x.....x.x...x.....x...x...x...x.....x.x...x','....x.xxxxx.xxxxx.....x.xxxxx.xxxxx.....x.......xxxxx.xxxxx.xxxxx']
caracter = []
numero = []
enteroMatriz = []
enteroNumero = []
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


for i in range(int(len(caracter[i])/6)+1):
	enteroMatriz.append([])
	for j in range(7):
		enteroMatriz[i].append(numero[j][i])	#ahora cada elemento enteroMatriz[i] representa un número distinto

for i in range(len(enteroMatriz)):
	if enteroMatriz[i] == uno:
		enteroNumero.append('1')
	elif enteroMatriz[i] == dos:
		enteroNumero.append('2')
	elif enteroMatriz[i] == tres:
		enteroNumero.append('3')
	elif enteroMatriz[i] == cuatro:
		enteroNumero.append('4')
	elif enteroMatriz[i] == cinco:
		enteroNumero.append('5')
	elif enteroMatriz[i] == seis:
		enteroNumero.append('6')
	elif enteroMatriz[i] == siete:
		enteroNumero.append('7')
	elif enteroMatriz[i] == ocho:
		enteroNumero.append('8')
	elif enteroMatriz[i] == nueve:
		enteroNumero.append('9')
	elif enteroMatriz[i] == signomas:
		enteroNumero.append('+')
	elif enteroMatriz[i] == signomenos:
		enteroNumero.append('-')
	elif enteroMatriz[i] == multiplicacion:
		enteroNumero.append('*')
	elif enteroMatriz[i] == division:
		enteroNumero.append('/')
	else:
		enteroNumero.append('0')


if enteroNumero.index('+')>0:
	indiceOperacion = enteroNumero.index('+')
	tipoOperacion = '+'
elif enteroNumero.index('-')>0:
	indiceOperacion = enteroNumero.index('-')
	tipoOperacion = '-'
elif enteroNumero.index('*')>0:
	indiceOperacion = enteroNumero.index('*')
	tipoOperacion = '*'
else:
	indiceOperacion = enteroNumero.index('/')
	tipoOperacion = '/'
for i in range(indiceOperacion):
	numeroSt1 = numeroSt1 + enteroNumero[i]
numero1 = int(numeroSt1)

for i in range(indiceOperacion+1, len(enteroNumero)):
	numeroSt2 = numeroSt2 + enteroNumero[i]
	
print (numeroSt1, numeroSt2)
print ('1'+'2'+'3')
#print (enteroMatriz[0])
#for i in (enteroMatriz[0]):
#	print (i)
#print (len(enteroMatriz))
#print(numero[0][0])
			

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
#	print (numero[i][9]) #numero_ij		#otra prueba


			