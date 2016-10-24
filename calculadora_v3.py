#Se crean los numeros y operadores ASCII
NUM0 = [['x','x','x','x','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','x','x','x','x']]
NUM1 = [['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x']]
NUM2 = [['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['x','x','x','x','x'],['x','.','.','.','.'],['x','.','.','.','.'],['x','x','x','x','x']]
NUM3 = [['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['x','x','x','x','x']]
NUM4 = [['x','.','.','.','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x']]
NUM5 = [['x','x','x','x','x'],['x','.','.','.','.'],['x','.','.','.','.'],['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['x','x','x','x','x']]
NUM6 = [['x','x','x','x','x'],['x','.','.','.','.'],['x','.','.','.','.'],['x','x','x','x','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','x','x','x','x']]
NUM7 = [['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x']]
NUM8 = [['x','x','x','x','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','x','x','x','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','x','x','x','x']]
NUM9 = [['x','x','x','x','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['x','x','x','x','x']]
SMAS = [['.','.','.','.','.'],['.','.','x','.','.'],['.','.','x','.','.'],['x','x','x','x','x'],['.','.','x','.','.'],['.','.','x','.','.'],['.','.','.','.','.']]
SMEN = [['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['x','x','x','x','x'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.']]
SMUL = [['.','.','.','.','.'],['x','.','.','.','x'],['.','x','.','x','.'],['.','.','x','.','.'],['.','x','.','x','.'],['x','.','.','.','x'],['.','.','.','.','.']]
SDIV = [['.','.','.','.','.'],['.','.','.','.','x'],['.','.','.','x','.'],['.','.','x','.','.'],['.','x','.','.','.'],['x','.','.','.','.'],['.','.','.','.','.']]
PUNT = [['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','x','.','.']]

#Transforma el string fila[i] en una fila de "n" elementos
def separarCaracteres(fila):
	caracter = []
	for i in range(7):	
		caracter.append([])
		caracter[i] = list(fila[i])
	return caracter

#Guarda un numero ASCII diferente en cada columna de la matriz numero[i][j]
def agruparCaracteres(caracter):
	numero = []
	for i in range(7):										
		numero.append([])
		for j in range(int(len(caracter[i])/6)+1):
			numero[i].append([])
			for k in range(5):
				numero[i][j].append(caracter[i][k+6*j])		
	return numero

#Cada elemento de enteroMatriz[i] representa un numero distinto
def agruparNumeros(numero):
	enteroMatriz = []
	for i in range(int(len(caracter[0])/6)+1):				
		enteroMatriz.append([])
		for j in range(7):
			enteroMatriz[i].append(numero[j][i])	
	return enteroMatriz

#Inserta un numero (u operacion) en forma de string dentro de la matriz enteroNumero
#que equivale al numero en formato ASCII en la posicion [i]	
def reemplazar(enteroMatriz):
	enteroNumero = []
	for i in range(len(enteroMatriz)):						
		if enteroMatriz[i] == NUM1:							
			enteroNumero.append('1')
		elif enteroMatriz[i] == NUM2:
			enteroNumero.append('2')
		elif enteroMatriz[i] == NUM3:
			enteroNumero.append('3')
		elif enteroMatriz[i] == NUM4:
			enteroNumero.append('4')
		elif enteroMatriz[i] == NUM5:
			enteroNumero.append('5')
		elif enteroMatriz[i] == NUM6:
			enteroNumero.append('6')
		elif enteroMatriz[i] == NUM7:
			enteroNumero.append('7')
		elif enteroMatriz[i] == NUM8:
			enteroNumero.append('8')
		elif enteroMatriz[i] == NUM9:
			enteroNumero.append('9')
		elif enteroMatriz[i] == SMAS:
			enteroNumero.append('+')
		elif enteroMatriz[i] == SMEN:
			enteroNumero.append('-')
		elif enteroMatriz[i] == SMUL:
			enteroNumero.append('*')
		elif enteroMatriz[i] == SDIV:
			enteroNumero.append('/')
		else:
			enteroNumero.append('0')
	return enteroNumero

#Ubica la posicion del operador 
def posicionOperador(enteroNumero):
	indiceOperacion = 0
	if '+' in enteroNumero:									
		indiceOperacion = enteroNumero.index('+')			
	elif '-' in enteroNumero:
		indiceOperacion = enteroNumero.index('-')
	elif '*' in enteroNumero:
		indiceOperacion = enteroNumero.index('*')
	else:
		indiceOperacion = enteroNumero.index('/')
	return indiceOperacion
	
#Indica que tipo de operacion se va a realizar
def operacion(enteroNumero):
	tipoOperacion = ''
	if '+' in enteroNumero:									
		tipoOperacion = '+'
	elif '-' in enteroNumero:
		tipoOperacion = '-'
	elif '*' in enteroNumero:
		tipoOperacion = '*'
	else:
		tipoOperacion = '/'
	return tipoOperacion

#Transforma los numeros a enteros y los opera	
def operar(enteroNumero, indiceOperacion, tipoOperacion):
	numeroSt1 = ''
	numeroSt2 = ''
	for i in range(indiceOperacion):						
		numeroSt1 = numeroSt1 + enteroNumero[i]
	primero = int(numeroSt1)
	
	for i in range(indiceOperacion+1, len(enteroNumero)):	
		numeroSt2 = numeroSt2 + enteroNumero[i]
	segundo = int(numeroSt2)
	
	if tipoOperacion == '+':								
		resultado = primero + segundo						
	elif tipoOperacion == '-':
		resultado = primero - segundo
	elif tipoOperacion == '*':
		resultado = primero * segundo
	else:
		resultado = float(primero) / float(segundo)
	return resultado

fila = ['....x.xxxxx.xxxxx.x...x.xxxxx.xxxxx.xxxxx.......xxxxx.xxxxx.xxxxx.....x','....x.....x.....x.x...x.x.....x.........x.....x.x...x.x...x.x...x.....x','....x.....x.....x.x...x.x.....x.........x....x..x...x.x...x.x...x.....x','....x.xxxxx.xxxxx.xxxxx.xxxxx.xxxxx.....x...x...xxxxx.xxxxx.x...x.....x','....x.x.........x.....x.....x.x...x.....x..x....x...x.....x.x...x.....x','....x.x.........x.....x.....x.x...x.....x.x.....x...x.....x.x...x.....x','....x.xxxxx.xxxxx.....x.xxxxx.xxxxx.....x.......xxxxx.xxxxx.xxxxx.....x']

caracter = separarCaracteres(fila)
numero = agruparCaracteres(caracter)
enteroMatriz = agruparNumeros(numero)
enteroNumero = reemplazar(enteroMatriz)
indiceOperacion = posicionOperador(enteroNumero)
tipoOperacion = operacion(enteroNumero)
resultado = operar(enteroNumero, indiceOperacion, tipoOperacion)

print(resultado)
