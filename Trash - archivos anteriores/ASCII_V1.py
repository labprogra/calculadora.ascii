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
ASCII = [NUM0,NUM1,NUM2,NUM3,NUM4,NUM5,NUM6,NUM7,NUM8,NUM9,SMAS,SMEN,SMUL,SDIV,PUNT]
STR = ['0','1','2','3','4','5','6','7','8','9','+','-','*','/','.']
ERROR = 'Archivo incorrecto'

#Abre un archivo con una operacion ASCII y asigna todas las filas dentro de distintos elementos de una lista
def leerArchivo():
        nombre = raw_input('Ingrese el nombre del archivo: ')
        nombre = nombre.strip(".txt")
        nombre = nombre + '.txt'
        archivo = open(nombre,'r')
        fila1 = []
        fila2 = []
        for i in range(7):
                fila1.append(archivo.readline())
                if i != 6:
                        fila2.append(fila1[i][0:len(fila1[i])-1])
                else:
                        fila2.append(fila1[i][0:len(fila1[i])])
                if (len(fila2[i]) + 1) % 6 != 0:
                        print ERROR
                        mensaje = 'El largo de alguna(s) fila(s) no corresponde(n) al requerido, modifique el archivo y reinicie el programa'
                        fila2 = ['xxxxx','x...x','x...x','x...x','x...x','x...x','xxxxx',mensaje]
                        break
        for i in range(1,6):
                if len(fila2[i]) != len(fila2[i-1]):
                        print ERROR
                        mensaje = 'Existen filas mas largas que otras, modifique el archivo y reinicie el programa'
                        fila2 = ['xxxxx','x...x','x...x','x...x','x...x','x...x','xxxxx',mensaje]
        return fila2

#Transforma el string fila[i] en una fila de "n" elementos (con n como el largo del string de fila[i])
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
		for j in range(len(ASCII)):
			if enteroMatriz[i] == ASCII[j]:
				enteroNumero.append(STR[j])
	return enteroNumero

#Ubica la posicion del operador 
def posicionOperador(enteroNumero):
	indiceOperacion = 1
	if '+' in enteroNumero:									
		indiceOperacion = enteroNumero.index('+')			
	elif '-' in enteroNumero:
		indiceOperacion = enteroNumero.index('-')
	elif '*' in enteroNumero:
		indiceOperacion = enteroNumero.index('*')
	elif '/' in enteroNumero:
		indiceOperacion = enteroNumero.index('/')
	return indiceOperacion
	
#Indica que tipo de operacion se va a realizar
def operacion(enteroNumero):
	tipoOperacion = '+'
	if '+' in enteroNumero:									
		tipoOperacion = '+'
	elif '-' in enteroNumero:
		tipoOperacion = '-'
	elif '*' in enteroNumero:
		tipoOperacion = '*'
	elif '/' in enteroNumero:
		tipoOperacion = '/'
	return tipoOperacion

#Transforma los numeros a enteros y los opera	
def operar(enteroNumero, indiceOperacion, tipoOperacion):
	numeroSt1 = ''
	numeroSt2 = ''
	for i in range(indiceOperacion):						
		numeroSt1 = numeroSt1 + enteroNumero[i]
	primero = int(numeroSt1)
	if indiceOperacion != 1:               
		for i in range(indiceOperacion+1, len(enteroNumero)):	
			numeroSt2 = numeroSt2 + enteroNumero[i]
	else:
		numeroSt2 = '0'
	segundo = int(numeroSt2)
	
	if tipoOperacion == '+':								
		resultado = primero + segundo						
	elif tipoOperacion == '-':
		resultado = primero - segundo
	elif tipoOperacion == '*':
		resultado = primero * segundo
	elif tipoOperacion == '/':
		if segundo != 0:
			resultado = float(primero) / float(segundo)
		else:
			resultado = 'No se puede dividir por cero'
	if resultado != 'No se puede dividir por cero':
		if resultado - int(resultado) == 0:
			resultado = int(resultado)
	return resultado

while True:
	try:
		fila = leerArchivo()
		caracter = separarCaracteres(fila)
		numero = agruparCaracteres(caracter)
		enteroMatriz = agruparNumeros(numero)
		enteroNumero = reemplazar(enteroMatriz)
		indiceOperacion = posicionOperador(enteroNumero)
		tipoOperacion = operacion(enteroNumero)
		resultado = operar(enteroNumero, indiceOperacion, tipoOperacion)
		if len(fila) == 8:
		        print fila[7]
		else:
		        print 'OPERACION'
		        for i in range(7):
		                print fila[i]
		        print 'RESULTADO'
		        print (resultado)
		        print "Presione ENTER para introducir un nuevo archivo y Q para salir"
		        verification = raw_input('')
		        if (verification == "q") or (verification == "Q"):
		        	break
		        else:
		        	continue
		input ()

	except SyntaxError:
		continue
	except NameError:
		continue

	except IOError:
		print "***!!!!!!!!!!!!!!!!!!!!!!***"
		print "NO se ha encontrado el archivo"
		print "por favor intentelo nuevamente \n"
		continue

	except IndexError:
		print "***!!!!!!!!!!!!!!!!!!!!!!***"
		print "el archivo contiene errores en su escritura"
		print "por favor intentelo nuevamente \n"
		continue
