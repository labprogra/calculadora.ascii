from sys import *
from Tkinter import *
import tkFont

class File:
	def __init__(self, name):
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

class AsciiToNumber:
	def __init__(self, row):
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

class Calculator:
	def __init__(self, intNumber, operationIndex, operationType):
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

class NumberToAscii:
	def __init__(self, number):
		#atributos
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
			self.decimalNumber = self.decimalNumber[1]+self.decimalNumber[2]+self.decimalNumber[3]
		except Exception as e:
			self.decimalNumber = ""
		self.finalNumber = self.intNumber+self.decimalNumber
		return self.finalNumber

	def numeroArreglo(self):
		self.finalNumber = str(self.finalNumber)
		for digito in self.finalNumber:
			self.arrayNumber.append(digito)
		return str(self.arrayNumber)

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


notFound = "NO se ha encontrado el archivo, por favor intente nuevamente"
notMatch = "el archivo no coincide  con nada almacenado \n este error probablemente se deba a un caracter mal ubicado"
line = "_________________________________________________________________________\n"
O = 'OPERACION\n'
R = 'RESULTADO\n'
failure = 'Archivo incorrecto'
rowError = 'El largo de alguna(s) fila(s) no corresponde(n) al requerido, modifique el archivo'
caracterError = "algun(os) caracter(es) no corresponde(n) a lo solicitado, modifique el archivo"

def main(event):
	try:
		name = box.get()
		file = File(name)
		fileInOneRow = file.leerArchivo()
		try:
			matrix = fileInOneRow[0]+"\n"+fileInOneRow[1]+"\n"+fileInOneRow[2]+"\n"+fileInOneRow[3]+"\n"+fileInOneRow[4]+"\n"+fileInOneRow[5]+"\n"+fileInOneRow[6]+"\n"
		except Exception as e:
			matrix = ""
		if file.validacion() == True:
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
			Operation.config(text=(line+O+line))
			Matriz.config(text=matrix)
			Result.config(text=(line+R+line))
			if resultado == "No se puede dividir por CERO":
				OUTPUT.config(text=resultado)
				print resultado
			else:
				OUTPUT.config(text=matrizResultado)
				print matrizResultado
			message.config(text="")
		else:
			if file.validacion() == ("\n" + failure + "\n" + rowError):
				message.config(text=(file.validacion()))
				Operation.config(text="")
				Result.config(text="")
				OUTPUT.config(text="")
				Matriz.config(text="")
			elif file.validacion() == ("\n" + failure + "\n" + caracterError):
				message.config(text=(file.validacion()))
				Operation.config(text="")
				Result.config(text="")
				OUTPUT.config(text="")
				Matriz.config(text="")
			print file.validacion()
			print fileInOneRow
	except SyntaxError:
		pass
	except NameError:
		pass
	except IOError:
		print notFound
		message.config(text=notFound)
		Operation.config(text="")
		Result.config(text="")
		OUTPUT.config(text="")
		Matriz.config(text="")
	except IndexError:
		print notMatch
		message.config(text=failure+"\n"+notMatch)
		Operation.config(text="")
		Result.config(text="")
		OUTPUT.config(text="")
		Matriz.config(text="")

#instancio el objeto de la GUI
root = Tk()
root.title("Calculadora ASCII")
root.bind("<Return>", main)

font = tkFont.Font(family="FixedSys", size=12)
calibri = tkFont.Font(family="Calibri Light", size=12)

root.geometry("1200x700")
leftFrame = Frame(root)
leftFrame.pack(pady = 50, padx = 50)

#texto de informacion
text = Label(leftFrame, text="Ingresar el nombre del archivo:")
text.grid(columnspan=10,row=0)
#caja de entrada de texto
box = Entry(leftFrame, textvariable="")
box.grid(columnspan=9,column=0,row=1)
#boton para buscar
submitFile = Button(leftFrame, text="Buscar", fg="black")
submitFile.bind("<Button-1>", main)
submitFile.grid(column=10,row=1)
#mensaje de error
message = Label(leftFrame, text="", font=calibri)
message.grid(columnspan=10, row=4)
#operacion titulo
Operation = Label(leftFrame, text="")
Operation.grid(columnspan=10, row=3)
#matriz de la operacion
Matriz = Label(leftFrame, text="", font=font)
Matriz.grid(columnspan=10, row=4)
#resultado titulo
Result = Label(leftFrame, text="")
Result.grid(columnspan=10, row=5)
#output, que deberia ser matriz resutado
OUTPUT = Label(leftFrame, text="", font=font)
OUTPUT.grid(columnspan=10, row=6)
#Status bar con la version del proyecto
status = Label(root, text="Version 1.0.2 - Calculadora ASCII", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()