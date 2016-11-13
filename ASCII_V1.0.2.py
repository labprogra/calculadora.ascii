from sys import *
from Tkinter import *
import tkFont

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

#__________________________________________________________FUNCIONES INTERFAZ GRAFICA_______________________________________________________________


#__________________________________________________________FUNCIONES PROGRAMA_______________________________________________________________________

#Abre un archivo con una operacion ASCII y asigna todas las filas dentro de distintos elementos de una lista
def leerArchivo(nombre):
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
                	error = True
                	return error
        for i in range(1,6):
                if len(fila2[i]) != len(fila2[i-1]):
                    error = True
                    return error
        return fila2

#Valida si el archivo esta correcto usando la funcion de leer archivo
def validation(fila):
	correct = True
	error = False
	if (fila == True):
		print ERROR
		a = 'El largo de alguna(s) fila(s) no corresponde(n) al requerido, modifique el archivo'
		print a
		correct = False
	else:
		for conjunto in fila:
			for letra in conjunto:
				if not((letra == ".")or(letra == "x")):
					error = True
	if error:
		print ERROR
		b = "algun(os) caracter(es) no corresponde(n) a lo solicitado, modifique el archivo"
		print b
		correct = "caracter erroneo"
	return correct

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
def agruparNumeros(numero, caracter):
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
	error = False

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
			resultado = "No se puede dividir por CERO"
	if (resultado != "No se puede dividir por CERO"):
		if (resultado - int(resultado)) == 0:
			resultado = int(resultado)
	return resultado

def main():
	try:
		FileName = box.get()
		fila = leerArchivo(FileName)
		correctFile = validation(fila)
		if (correctFile == True):
			caracter = separarCaracteres(fila)
			numero = agruparCaracteres(caracter)
			enteroMatriz = agruparNumeros(numero, caracter)
			enteroNumero = reemplazar(enteroMatriz)
			indiceOperacion = posicionOperador(enteroNumero)
			tipoOperacion = operacion(enteroNumero)
			resultado = operar(enteroNumero, indiceOperacion, tipoOperacion)
			if len(fila) == 8:
			        print fila[7]
			else:
				line = "_________________________________________________________________________\n"
				O = 'OPERACION\n'
				R = 'RESULTADO\n'
				print (line+O+line)
				Operation.config(text=(line+O+line))
		        matriz = fila[0]+"\n"+fila[1]+"\n"+fila[2]+"\n"+fila[3]+"\n"+fila[4]+"\n"+fila[5]+"\n"+fila[6]+"\n"
		        print matriz
		        Matriz.config(text=matriz)
		        Result.config(text=(line+R+line))
		        OUTPUT.config(text=resultado)
		        message.config(text="")
		        print (line+R+line)
		        print (resultado)
		        print "\n"
		elif (correctFile == "caracter erroneo"):
			caracterError = "algun(os) caracter(es) no corresponde(n) a lo solicitado, modifique el archivo"
			message.config(text=(ERROR+caracterError))
		elif (correctFile == False):
			filaError = 'El largo de alguna(s) fila(s) no corresponde(n) al requerido, modifique el archivo'
			message.config(text=(ERROR+filaError))

	except SyntaxError:
		pass
	except NameError:
		pass
	except IOError:
		error = "NO se ha encontrado el archivo    , por favor intente nuevamente"
		message.config(text=error)
		Operation.config(text="")
		Result.config(text="")
		OUTPUT.config(text="")
		Matriz.config(text="")

	except IndexError:
		a = "el archivo no coincide  con nada almacenado"
		b = "este error probablemente se deba a un caracter mal ubicado"
		message.config(text=ERROR+"\n"+a+"\n"+b)
		Operation.config(text="")
		Result.config(text="")
		OUTPUT.config(text="")
		Matriz.config(text="")


#instancio el objeto de la GUI
root = Tk()
root.title("Calculadora ASCII")

font = tkFont.Font(family="FixedSys", size=12)
calibri = tkFont.Font(family="Calibri Light", size=12)

root.geometry("1200x500")
leftFrame = Frame(root)
leftFrame.pack(pady = 50, padx = 50)

#______________________________________________INICIAL________________________

#texto de informacion
text = Label(leftFrame, text="Ingresar el nombre del archivo:")
text.grid(columnspan=2,row=0)

#caja de entrada de texto
box = Entry(leftFrame, textvariable="")
box.grid(row=1)

#boton para buscar
submitFile = Button(leftFrame, text="Buscar", fg="black", command=main)
submitFile.grid(column=1,row=1)

#_____________________________________________________________________________

#mensaje de error
message = Label(leftFrame, text="", font=calibri)
message.grid(columnspan=2, row=4)

#operacion titulo
Operation = Label(leftFrame, text="")
Operation.grid(columnspan=3, row=3)

#matriz de la operacion
Matriz = Label(leftFrame, text="", font=font)
Matriz.grid(columnspan=7, row=4)

#resultado titulo
Result = Label(leftFrame, text="")
Result.grid(columnspan=3, row=5)

#output, que deberia ser matriz resutado
OUTPUT = Label(leftFrame, text="")
OUTPUT.grid(columnspan=3, row=6)

#Status bar con la version del proyecto
status = Label(root, text="Version 1.0.2 - Calculadora ASCII", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)



root.mainloop()