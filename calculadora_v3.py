#Acá se crean los números y operadores ASCII
num1 = [['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x']]
num2 = [['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['x','x','x','x','x'],['x','.','.','.','.'],['x','.','.','.','.'],['x','x','x','x','x']]
num3 = [['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['x','x','x','x','x']]
num4 = [['x','.','.','.','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x']]
num5 = [['x','x','x','x','x'],['x','.','.','.','.'],['x','.','.','.','.'],['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['x','x','x','x','x']]
num6 = [['x','x','x','x','x'],['x','.','.','.','.'],['x','.','.','.','.'],['x','x','x','x','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','x','x','x','x']]
num7 = [['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x']]
num8 = [['x','x','x','x','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','x','x','x','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','x','x','x','x']]
num9 = [['x','x','x','x','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['x','x','x','x','x']]
sMas = [['.','.','.','.','.'],['.','.','x','.','.'],['.','.','x','.','.'],['x','x','x','x','x'],['.','.','x','.','.'],['.','.','x','.','.'],['.','.','.','.','.']]
sMen = [['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['x','x','x','x','x'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.']]
sMul = [['.','.','.','.','.'],['x','.','.','.','x'],['.','x','.','x','.'],['.','.','x','.','.'],['.','x','.','x','.'],['x','.','.','.','x'],['.','.','.','.','.']]
sDiv = [['.','.','.','.','.'],['.','.','.','.','x'],['.','.','.','x','.'],['.','.','x','.','.'],['.','x','.','.','.'],['x','.','.','.','.'],['.','.','.','.','.']]
punt = [['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','x','.','.']]
#Creación de variables
indiceOperacion = 0
tipoOperacion = ''
numeroSt1 = ''
numeroSt2 = ''
primero = 0
segundo = 0
resultado = 0
resultadoDiv = 0.0
caracter = []
numero = []
enteroMatriz = []
enteroNumero = []

fila = ['....x.xxxxx.xxxxx.x...x.xxxxx.xxxxx.xxxxx.......xxxxx.xxxxx.xxxxx.....x','....x.....x.....x.x...x.x.....x.........x.....x.x...x.x...x.x...x.....x','....x.....x.....x.x...x.x.....x.........x....x..x...x.x...x.x...x.....x','....x.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.....x...x...xxxxx.xxxxx.x...x.....x','....x.x.........x.....x.....x.x...x.....x..x....x...x.....x.x...x.....x','....x.x.........x.....x.....x.x...x.....x.x.....x...x.....x.x...x.....x','....x.xxxxx.xxxxx.....x.xxxxx.xxxxx.....x.......xxxxx.xxxxx.xxxxx.....x']
for i in range(7):										#Aquí se transforma el string fila[i] en una fila de "n" elementos
	caracter.append([])
	caracter[i] = list(fila[i])

for i in range(7):										#Con este for se guarda un numero ASCII diferente en cada columna de la matriz numero[i][j]
	numero.append([])
	for j in range(int(len(caracter[i])/6)+1):
		numero[i].append([])
		for k in range(5):
			numero[i][j].append(caracter[i][k+6*j])		


for i in range(int(len(caracter[i])/6)+1):				#Ahora cada elemento de enteroMatriz[i] representa un número distinto
	enteroMatriz.append([])
	for j in range(7):
		enteroMatriz[i].append(numero[j][i])	

for i in range(len(enteroMatriz)):						#Esta condición inserta un numero (u operación) en forma de string dentro de la matriz enteroNumero
	if enteroMatriz[i] == num1:							#que equivale al número en formato ASCII en a posición [i]
		enteroNumero.append('1')
	elif enteroMatriz[i] == num2:
		enteroNumero.append('2')
	elif enteroMatriz[i] == num3:
		enteroNumero.append('3')
	elif enteroMatriz[i] == num4:
		enteroNumero.append('4')
	elif enteroMatriz[i] == num5:
		enteroNumero.append('5')
	elif enteroMatriz[i] == num6:
		enteroNumero.append('6')
	elif enteroMatriz[i] == num7:
		enteroNumero.append('7')
	elif enteroMatriz[i] == num8:
		enteroNumero.append('8')
	elif enteroMatriz[i] == num9:
		enteroNumero.append('9')
	elif enteroMatriz[i] == sMas:
		enteroNumero.append('+')
	elif enteroMatriz[i] == sMen:
		enteroNumero.append('-')
	elif enteroMatriz[i] == sMul:
		enteroNumero.append('*')
	elif enteroMatriz[i] == sDiv:
		enteroNumero.append('/')
	else:
		enteroNumero.append('0')


if '+' in enteroNumero:									#Este if lo que hace es ubicar la posición del operador 
	indiceOperacion = enteroNumero.index('+')			#E indicar que tipo de operación se va a realizar
	tipoOperacion = '+'
elif '-' in enteroNumero:
	indiceOperacion = enteroNumero.index('-')
	tipoOperacion = '-'
elif '*' in enteroNumero:
	indiceOperacion = enteroNumero.index('*')
	tipoOperacion = '*'
else:
	indiceOperacion = enteroNumero.index('/')
	tipoOperacion = '/'
for i in range(indiceOperacion):						#Este ciclo crea el primer número de la operación
	numeroSt1 = numeroSt1 + enteroNumero[i]
primero = int(numeroSt1)

for i in range(indiceOperacion+1, len(enteroNumero)):	#Este ciclo crea el segundo número de la operación
	numeroSt2 = numeroSt2 + enteroNumero[i]
segundo = int(numeroSt2)

if tipoOperacion == '+':								#Con esta condición se logra operar los num2 números
	resultado = primero + segundo						#Cuando la operación es una división los números enteros se transforman en float
elif tipoOperacion == '-':
	resultado = primero - segundo
elif tipoOperacion == '*':
	resultado = primero * segundo
else:
	resultadoDiv = float(primero) / float(segundo)
print (numeroSt1),
print(tipoOperacion),
print(numeroSt2),
print('='),
if tipoOperacion != '/':
	print(resultado)
else:
	print(resultadoDiv)