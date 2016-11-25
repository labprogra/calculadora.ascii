
"""
----  primero importamos sys para poder acceder a permisos de la computadora
----- luego Tkinter nos permite crear una interfaz grafica
----- tkFont nos permite cambiar las fuentes de la interfaz grafica, es necesario ya que las matrices necesitan la fuente FixedSys
----- tkMessageBox es un modulo que nos permite lanzar diversos mensajes al usuario en forma de cajas
"""

from sys import *
from Tkinter import *
import tkFont
import tkMessageBox

#_____________________________________________________________________________________________________________________________________________________________#

#la clase archivo es un bloque de codigo que guarda todo lo que tenga que ver con archivos
class File:
	def __init__(self, name):
		#todas las variables que se usan dentro de esta clase van colocadas aqui
		self.name = name
		self.name = self.name.strip(".txt")
		self.name = self.name + '.txt'
		self.file = open(self.name,'r')
		self.row1 = []
		self.row2 = []
		self.check = True
		self.error = False
		self.failure = 'Archivo incorrecto'
		self.rowError = 'El largo de alguna(s) fila(s) no corresponde(n) al requerido, modifique el archivo'
		self.caracterError = "algun(os) caracter(es) no corresponde(n) a lo solicitado, modifique el archivo"
		self.message = ""

	#esta funcion lee un archivo de texto y verifica si existe, en caso de existir retorna todo el documento en una sola linea
	def leerArchivo(self):
		for i in range(7):
			self.row1.append(self.file.readline())
			if i != 6:
				self.row2.append(self.row1[i][0:len(self.row1[i])-1])
			else:
				self.row2.append(self.row1[i][0:len(self.row1[i])])
			if (len(self.row2[i]) + 1) % 6 != 0:
				self.row2 = True
				return self.row2
		for i in range(1,6):
			if len(self.row2[i]) != len(self.row2[i-1]):
				self.row2 = True
				return self.row2
		return self.row2

	#toma la linea del documento y verifica que todo este en orden junto con revisar si solo consta de puntos y equis
	def validacion(self):
		if (self.row2 == True):
			self.message = ""
			self.message += "\n" + self.failure + "\n" + self.rowError
			self.check = False
			return self.message
		else:
			for conjunto in self.row2:
				for letra in conjunto:
					if not((letra == ".")or(letra == "x")):
						self.error = True
		if self.error:
			self.message = ""
			self.message += "\n" + self.failure + "\n" + self.caracterError
			return self.message
		return self.check


#_____________________________________________________________________________________________________________________________________________________________#

#esta clase se encarga de tomar el documento ASCII y transformarlo a un numero entero
class AsciiToNumber:
	def __init__(self, row):
		#aqui van todas las variables que se usaran en las funciones mas adelante
		self.NUM0 = [['x','x','x','x','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','x','x','x','x']]
		self.NUM1 = [['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x']]
		self.NUM2 = [['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['x','x','x','x','x'],['x','.','.','.','.'],['x','.','.','.','.'],['x','x','x','x','x']]
		self.NUM3 = [['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['x','x','x','x','x']]
		self.NUM4 = [['x','.','.','.','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x']]
		self.NUM5 = [['x','x','x','x','x'],['x','.','.','.','.'],['x','.','.','.','.'],['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['x','x','x','x','x']]
		self.NUM6 = [['x','x','x','x','x'],['x','.','.','.','.'],['x','.','.','.','.'],['x','x','x','x','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','x','x','x','x']]
		self.NUM7 = [['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x'],['.','.','.','.','x']]
		self.NUM8 = [['x','x','x','x','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','x','x','x','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','x','x','x','x']]
		self.NUM9 = [['x','x','x','x','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','x','x','x','x'],['.','.','.','.','x'],['.','.','.','.','x'],['x','x','x','x','x']]
		self.SMAS = [['.','.','.','.','.'],['.','.','x','.','.'],['.','.','x','.','.'],['x','x','x','x','x'],['.','.','x','.','.'],['.','.','x','.','.'],['.','.','.','.','.']]
		self.SMEN = [['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['x','x','x','x','x'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.']]
		self.SMUL = [['.','.','.','.','.'],['x','.','.','.','x'],['.','x','.','x','.'],['.','.','x','.','.'],['.','x','.','x','.'],['x','.','.','.','x'],['.','.','.','.','.']]
		self.SDIV = [['.','.','.','.','.'],['.','.','.','.','x'],['.','.','.','x','.'],['.','.','x','.','.'],['.','x','.','.','.'],['x','.','.','.','.'],['.','.','.','.','.']]
		self.PUNT = [['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','.','.','.'],['.','.','x','.','.']]
		self.caracter = []
		self.row = row
		self.number = []
		self.intMatrix = []
		self.intNumber = []
		self.ASCII = [self.NUM0,self.NUM1,self.NUM2,self.NUM3,self.NUM4,self.NUM5,self.NUM6,self.NUM7,self.NUM8,self.NUM9,self.SMAS,self.SMEN,self.SMUL,self.SDIV,self.PUNT]
		self.STR = ['0','1','2','3','4','5','6','7','8','9','+','-','*','/','.']
		self.operationIndex = 1
		self.operationType = '+'

	def separarCaracteres(self):
		for i in range(7):
			self.caracter.append([])
			self.caracter[i] = list(self.row[i])
		return self.caracter

	def agruparCaracteres(self):
		for i in range(7):
			self.number.append([])
			for j in range(int(len(self.caracter[i])/6)+1):
				self.number[i].append([])
				for k in range(5):
					self.number[i][j].append(self.caracter[i][k+6*j])
		return self.number

	def agruparNumeros(self):
		for i in range(int(len(self.caracter[0])/6)+1):
			self.intMatrix.append([])
			for j in range(7):
				self.intMatrix[i].append(self.number[j][i])
		return self.intMatrix

	def reemplazar(self):
		for i in range(len(self.intMatrix)):
			for j in range(len(self.ASCII)):
				if self.intMatrix[i] == self.ASCII[j]:
					self.intNumber.append(self.STR[j])
		return self.intNumber

	def posicionOperador(self):
		if '+' in self.intNumber:
			self.operationIndex = self.intNumber.index('+')
		elif '-' in self.intNumber:
			self.operationIndex = self.intNumber.index('-')
		elif '*' in self.intNumber:
			self.operationIndex = self.intNumber.index('*')
		elif '/' in self.intNumber:
			self.operationIndex = self.intNumber.index('/')
		return self.operationIndex

	def operacion(self):
		if '+' in self.intNumber:
			self.operationType = '+'
		elif '-' in self.intNumber:
			self.operationType = '-'
		elif '*' in self.intNumber:
			self.operationType = '*'
		elif '/' in self.intNumber:
			self.operationType = '/'
		return self.operationType

#_____________________________________________________________________________________________________________________________________________________________#

#esta clase recibe los numeros enteros y se encarga de realizar la operacion matematica necesario y dar el error correspondiente si se divide por cero
class Calculator:
	def __init__(self, intNumber, operationIndex, operationType):
		#aqui van todas las variables que se usan en la funcion de esta clase
		self.numberSt1 = ''
		self.numberSt2 = ''
		self.error = False
		self.intNumber = intNumber
		self.operationIndex = operationIndex
		self.operationType = operationType
		self.result = ""
		self.first = ""
		self.second = ""

	def calculadora(self):
		for i in range(self.operationIndex):
			self.numberSt1 = self.numberSt1 + self.intNumber[i]
		self.first = int(self.numberSt1)
		if self.operationIndex != 1:
			for i in range(self.operationIndex+1, len(self.intNumber)):
				self.numberSt2 = self.numberSt2 + self.intNumber[i]
		else:
			self.numberSt2 = '0'
		self.second = int(self.numberSt2)
		if self.operationType == '+':
			self.result = self.first + self.second
		elif self.operationType == '-':
			self.result = self.first - self.second
		elif self.operationType == '*':
			self.result = self.first * self.second
		elif self.operationType == '/':
			if self.second != 0:
				self.result = float(self.first) / float(self.second)
			else:
				self.result = "No se puede dividir por CERO"
		if (self.result != "No se puede dividir por CERO"):
			if (self.result - int(self.result)) == 0:
				self.result = int(self.result)
		return self.result

#_____________________________________________________________________________________________________________________________________________________________#

#esta clase se encarga de recibir un numero entero o decimal y transformarlo a ASCII
class NumberToAscii:
	def __init__(self, number):
		#estas son las variables que se utilizaran en las funciones de esta clase
		self.number = number
		self.NUM0 = ['xxxxx','x...x','x...x','x...x','x...x','x...x','xxxxx']
		self.NUM1 = ['....x','....x','....x','....x','....x','....x','....x']
		self.NUM2 = ['xxxxx','....x','....x','xxxxx','x....','x....','xxxxx']
		self.NUM3 = ['xxxxx','....x','....x','xxxxx','....x','....x','xxxxx']
		self.NUM4 = ['x...x','x...x','x...x','xxxxx','....x','....x','....x']
		self.NUM5 = ['xxxxx','x....','x....','xxxxx','....x','....x','xxxxx']
		self.NUM6 = ['xxxxx','x....','x....','xxxxx','x...x','x...x','xxxxx']
		self.NUM7 = ['xxxxx','....x','....x','....x','....x','....x','....x']
		self.NUM8 = ['xxxxx','x...x','x...x','xxxxx','x...x','x...x','xxxxx']
		self.NUM9 = ['xxxxx','x...x','x...x','xxxxx','....x','....x','xxxxx']
		self.SMEN = ['.....','.....','.....','xxxxx','.....','.....','.....']
		self.PUNT = ['.....','.....','.....','.....','.....','.....','..x..']
		self.decimalNumber = ""
		self.decimal = False
		self.intNumber = ""
		self.finalNumber = ""
		self.asciiMatrix = []
		self.arrayNumber = []
		self.row1 = []
		self.row2 = []
		self.row3 = []
		self.row4 = []
		self.row5 = []
		self.row6 = []
		self.row7 = []
		self.finalMatrix = []
		self.fila1 = ""
		self.fila2 = ""
		self.fila3 = ""
		self.fila4 = ""
		self.fila5 = ""
		self.fila6 = ""
		self.fila7 = ""
		#contadores
		self.a = 0
		self.b = 0
		self.c = 0
		self.d = 0
		self.e = 0
		self.f = 0
		self.g = 0
		self.zeroDivision = False

	#esta funcion corta a cuatro decimales el numero
	def cortarDecimales(self):
		self.number = str(self.number)
		for digit in self.number:
			if not(self.decimal):
				self.intNumber += digit

			if digit == ".":
				self.decimal = True

			if self.decimal:
				self.decimalNumber += digit
		try:
			self.decimalNumber = self.decimalNumber[1]+self.decimalNumber[2]+self.decimalNumber[3]+self.decimalNumber[4]
		except Exception as e:
			self.decimalNumber = ""
		self.finalNumber = self.intNumber+self.decimalNumber
		return self.finalNumber

	#el numero entero o decimal se guarda en un arreglo, cada digito por separado
	def numeroArreglo(self):
		self.finalNumber = str(self.finalNumber)
		for digito in self.finalNumber:
			self.arrayNumber.append(digito)
		return str(self.arrayNumber)

	#este verifica cada digito por separado y lo reemplaza por la constante correspondiente previamente declarada en ASCII
	def asciiArreglo(self):
		for digito in self.arrayNumber:
			if digito == '-':
				self.asciiMatrix.append(self.SMEN)
			elif digito == '.':
				self.asciiMatrix.append(self.PUNT)
			elif digito == '0':
				self.asciiMatrix.append(self.NUM0)
			elif digito == '1':
				self.asciiMatrix.append(self.NUM1)
			elif digito == '2':
				self.asciiMatrix.append(self.NUM2)
			elif digito == '3':
				self.asciiMatrix.append(self.NUM3)
			elif digito == '4':
				self.asciiMatrix.append(self.NUM4)
			elif digito == '5':
				self.asciiMatrix.append(self.NUM5)
			elif digito == '6':
				self.asciiMatrix.append(self.NUM6)
			elif digito == '7':
				self.asciiMatrix.append(self.NUM7)
			elif digito == '8':
				self.asciiMatrix.append(self.NUM8)
			elif digito == '9':
				self.asciiMatrix.append(self.NUM9)
		return self.asciiMatrix

	#esta funcion ordena los elementos de manera que podamos tener 7 filas totalmente ordenadas e identificadas para poder saber que numero se trata
	def ordenarMatriz(self):
		for num in self.asciiMatrix:
			self.row1.append(num[0])
		for num in self.asciiMatrix:
			self.row2.append(num[1])
		for num in self.asciiMatrix:
			self.row3.append(num[2])
		for num in self.asciiMatrix:
			self.row4.append(num[3])
		for num in self.asciiMatrix:
			self.row5.append(num[4])
		for num in self.asciiMatrix:
			self.row6.append(num[5])
		for num in self.asciiMatrix:
			self.row7.append(num[6])
		self.finalMatrix = str(self.row1)+'\n'+str(self.row2)+'\n'+str(self.row3)+'\n'+str(self.row4)+'\n'+str(self.row5)+'\n'+str(self.row6)+'\n'+str(self.row7)
		return self.finalMatrix

	#una ves que tenemos las 7 filas solo tenemos que pasarlas a un string para poder imprimirla en pantalla
	def matrizAstring(self):
		for fila in self.row1:
			self.fila1 += str(self.row1[self.a])+"."
			self.a += 1
		for fila in self.row2:
			self.fila2 += str(self.row2[self.b])+"."
			self.b += 1
		for fila in self.row3:
			self.fila3 += str(self.row3[self.c])+"."
			self.c += 1
		for fila in self.row4:
			self.fila4 += str(self.row4[self.d])+"."
			self.d += 1
		for fila in self.row5:
			self.fila5 += str(self.row5[self.e])+"."
			self.e += 1
		for fila in self.row6:
			self.fila6 += str(self.row6[self.f])+"."
			self.f += 1
		for fila in self.row7:
			self.fila7 += str(self.row7[self.g])+"."
			self.g += 1
		self.fila1 = self.fila1[0:-1]
		self.fila2 = self.fila2[0:-1]
		self.fila3 = self.fila3[0:-1]
		self.fila4 = self.fila4[0:-1]
		self.fila5 = self.fila5[0:-1]
		self.fila6 = self.fila6[0:-1]
		self.fila7 = self.fila7[0:-1]

		self.finalMatrix = self.fila1+'\n'+self.fila2+'\n'+self.fila3+'\n'+self.fila4+'\n'+self.fila5+'\n'+self.fila6+'\n'+self.fila7
		return self.finalMatrix

#_____________________________________________________________________________________________________________________________________________________________#


#estas son constantes que se utilizan en el programa, se juntaron todas aqui con el proposito de acceder facilmente a ellas en caso de cambiar algo
notFound = "NO se ha encontrado el archivo, por favor intente nuevamente"
notMatch = "el archivo no coincide con nada almacenado \n este error probablemente se deba a un caracter mal ubicado"
line = "_________________________________________________________________________\n"
O = 'OPERACION\n'
R = 'RESULTADO\n'
failure = 'Archivo incorrecto'
rowError = 'El largo de alguna(s) fila(s) no corresponde(n) al requerido, modifique el archivo'
caracterError = "algun(os) caracter(es) no corresponde(n) a lo solicitado, modifique el archivo"

#_____________________________________________________________________________________________________________________________________________________________#

#Esta funcion main es la principal que funciona en caso de que el usuario presione la tecla ENTER o tambien cuando haga un click en el boton buscar
def main(event):
	#try quiere decir que el programa intentara ejecutar el codigo y en caso de cualquier error pasara a los bloques siguientes de codigo en ves de cerrarlo
	try:
		#la primera linea a continuacion actua como si fuese el raw_input anterior, ya que se encarga de recibir el texto desde la caja en la interfaz
		name = box.get()
		file = File(name)
		fileInOneRow = file.leerArchivo()
		try:
			#se ocupo un try aqui ya que en caso de ocurrir un error el programa no tiene que mostrar la matriz
			matrix = fileInOneRow[0]+"\n"+fileInOneRow[1]+"\n"+fileInOneRow[2]+"\n"+fileInOneRow[3]+"\n"+fileInOneRow[4]+"\n"+fileInOneRow[5]+"\n"+fileInOneRow[6]+"\n"
		except Exception as e:
			#por eso se encuentra vacia aqui
			matrix = ""
		if file.validacion() == True:
			#si la validacion fue exitosa entonces empieza ejecutando todas las funciones una por una en orden tal y como las venias leyendo
			print "el archivo no contiene ningun error"
			asciiToNumber = AsciiToNumber(fileInOneRow)
			caracter = asciiToNumber.separarCaracteres()
			number = asciiToNumber.agruparCaracteres()
			intMatrix = asciiToNumber.agruparNumeros()
			intNumber = asciiToNumber.reemplazar()
			operationIndex = asciiToNumber.posicionOperador()
			operationType = asciiToNumber.operacion()
			calculator = Calculator(intNumber, operationIndex, operationType)
			resultado = calculator.calculadora()
			print (line+O+line)
			print matrix
			print (line+R+line)
			numeroAscii = NumberToAscii(resultado)
			cortarDecimales = numeroAscii.cortarDecimales()
			numeroArreglo = numeroAscii.numeroArreglo()
			asciiArreglo = numeroAscii.asciiArreglo()
			ordenarMatriz = numeroAscii.ordenarMatriz()
			matrizResultado = numeroAscii.matrizAstring()
			#aqui es donde se muestra en la interfaz los datos
			Operation.config(text=(line+O+line))
			Matriz.config(text=matrix)
			Result.config(text=(line+R+line))
			if resultado == "No se puede dividir por CERO":
				#en caso de que la calculadora, la cual es la que se encarga de retornar el resultado, haya llegado a errorZeroDivision
				#entonces se muestra en pantalla el error de no se puede dividir por cero
				OUTPUT.config(text=resultado)
				print resultado
			else:
				#en caso de que no exista ese error muestra por pantalla la matriz
				OUTPUT.config(text=matrizResultado)
				print matrizResultado
			#al final el mensaje principal se reinicia por seacaso ocurra un error no lo muestre al usuario
			message.config(text="")
		else:
			#si la validacion fallo, existen dos tipos de error
			#error de fila, cuando una o varias son mas largas que las otras
			if file.validacion() == ("\n" + failure + "\n" + rowError):
				#abre una ventana aparte que muestra el error y vacia todos los demas textos en pantalla
				tkMessageBox.showwarning("warning", (file.validacion()))
				message.config(text="")
				Operation.config(text="")
				Result.config(text="")
				OUTPUT.config(text="")
				Matriz.config(text="")
			elif file.validacion() == ("\n" + failure + "\n" + caracterError):
				#error de caracter, en caso de que haya un caracter que no coincida con un punto o una equis
				#abre una ventana aparte que muestra el error y vacia todos los demas textos en pantalla
				tkMessageBox.showwarning("warning", (file.validacion()))
				message.config(text="")
				Operation.config(text="")
				Result.config(text="")
				OUTPUT.config(text="")
				Matriz.config(text="")
			print file.validacion()
			print fileInOneRow
	except SyntaxError:
		#quiere decir que en caso de que exista un error de sintaxis solo reinicie el programa
		pass
	except NameError:
		#quiere decir que en caso de que el usuario haya escrito mal algun nombre reinicie el programa para evitar complicaciones
		pass
	except IOError:
		#IOError es el error que lanza cuando no se encuentra el archivo, por tanto en el caso de surgir este error
		print notFound
		#se imprime esta ventana mostrando el mensaje notFound de las constantes
		tkMessageBox.showerror("Error", notFound)
		#todas estas lineas son para que cuando de un error todos los textos que estan en la interfaz se vacien y no muestre nada de un archivo anterior
		message.config(text="")
		Operation.config(text="")
		Result.config(text="")
		OUTPUT.config(text="")
		Matriz.config(text="")
	except IndexError:
		#al igual que con la anterior pero cuando da IndexError significa que la matriz no coincidio con ninguna guardada en nuestros datos
		print notMatch
		#muestra el mensaje al usuario de notMatch en las constantes
		tkMessageBox.showwarning("warning", failure+"\n"+notMatch)
		#vacia todos los textos en pantalla
		message.config(text="")
		Operation.config(text="")
		Result.config(text="")
		OUTPUT.config(text="")
		Matriz.config(text="")

#_____________________________________________________________________________________________________________________________________________________________#

#esta funcion se ejecuta cuando el usuario presiona el boton de ayuda y le muestra un breve resumen junto con instrucciones de como proceder
def instrucciones():
	instrucciones1 = "-ingresa el nombre del archivo en la caja de texto. \nEl archivo debe contener reglas basicas en formato ASCII para ser leido\n"
	instrucciones2 = "se realizara el proceso matematico correspondiente \nse mostrara en pantalla el resultado obtenido"
	tkMessageBox.showinfo("instrucciones", instrucciones1+instrucciones2)

#_____________________________________________________________________________________________________________________________________________________________#


#primero se crea la variable de mi ventana principal llamada root
root = Tk()
#le agrego un titulo a mi ventana
root.title("Calculadora ASCII")
#luego mapeo la tecla ENTER para que ejecute la funcion main y haga el papel del boton buscar
root.bind("<Return>", main)
# en Sistemas Operativos de linux no permite cambiar el icono de la ventana por lo que podemos detectar si el usuario lo abre desde linux o windows
# con un simple try, de abrir el programa en linux se le mostrara un mensaje explicandole el fallo y recomendandole abrirlo en windows
try:
	ubuntu = False
 	root.iconbitmap('icon.ico')
except Exception as e:
	ubuntu = True
 	tkMessageBox.showinfo("linux detectado", "debido a que usas una distro de linux nos es imposible cambiar \n el icono de la ventana, para una proxima ves en windows funcionara mucho mejor")

#fuentes
#para ubuntu u otra distro de linux debes descargar una fuente monoespaciada, en este caso se usa anonymous pro para ubuntu
#se descarga desde: http://www.marksimonson.com/fonts/view/anonymous-pro
#se copia con permisos root en la carpeta /usr/share/fonts 

if ubuntu:
	font = tkFont.Font(family="AnonymousPro", size=12)
else:
	font = tkFont.Font(family="FixedSys", size=12)

#y calibri light para los textos por que se me hace bonita
calibri = tkFont.Font(family="Calibri Light", size=12)
leftFrame = Frame(root)
leftFrame.pack(pady = 50, padx = 50)

#aqui es donde se guarda la imagen del logo de la usach en la variable logo, se le asigna una etiqueta para poder colocarla en pantalla
logo = PhotoImage(file="logo.gif")
usach = Label(root, image=logo)
usach.pack(side=TOP)

#texto que le dice al usuario que ingrese el nombre del archivo
text = Label(leftFrame, text="Ingresar el nombre del archivo:")
text.grid(row=0,sticky=W+E+N+S)

#caja de entrada de texto para que el usuario inserte el nombre del archivo
box = Entry(leftFrame, textvariable="")
box.grid(column=0,row=1,sticky=W+E+N+S)

#boton para buscar que esta mapeado para que cuando haga click ejecute la funcion main
submitFile = Button(leftFrame, text="Buscar", fg="black")
submitFile.bind("<Button-1>", main)
submitFile.grid(column=0,row=2,sticky=W+E+N+S)

#boton de ayuda para que cuando se le haga click ejecute la funcion instrucciones
HELP = Button(leftFrame, text="ayuda", fg="black", command = instrucciones)
HELP.grid(column=0,row=3,sticky=W+E+N+S)

#mensaje  aleatorio que se usa como resguardo en caso de que alguno falle, o no se muestre
message = Label(leftFrame, text="", font=calibri)
message.grid(row=5,sticky=W+E+N+S)

#operacion titulo
Operation = Label(leftFrame, text="")
Operation.grid(row=4,sticky=W+E+N+S)
#matriz de la operacion
Matriz = Label(leftFrame, text="", font=font)
Matriz.grid(row=5,sticky=W+E+N+S)
#resultado titulo
Result = Label(leftFrame, text="")
Result.grid(row=6,sticky=W+E+N+S)
#esta es la matriz final en la salida
OUTPUT = Label(leftFrame, text="", font=font)
OUTPUT.grid(row=7,sticky=W+E+N+S)
#Status bar con la version del proyecto
status = Label(root, text="Version 2.1.0 - Calculadora ASCII", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
#_____________________________________________________________________________________________________________________________________________________________#