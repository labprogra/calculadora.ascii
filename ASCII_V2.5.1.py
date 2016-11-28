
"""
----  primero importamos sys para poder acceder a permisos de la computadora
----- luego Tkinter nos permite crear una interfaz grafica
----- tkFont nos permite cambiar las fuentes de la interfaz grafica, es necesario ya que las matrices necesitan la fuente FixedSys
----- tkMessageBox es un modulo que nos permite lanzar diversos mensajes al usuario en forma de cajas
----- tkFileDialog nos permite crear una ventana extra para buscar archivos en el computador
"""

from sys import *
from Tkinter import *
import tkFont
import tkMessageBox
from tkFileDialog import *

#_____________________________________________________________________________________________________________________________________________________________#

#FUNCIONES QUE SE ENCARGAN DEL ARCHIVO
	
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
			fila2 = True
			return fila2
	for i in range(1,6):
		if len(fila2[i]) != len(fila2[i-1]):
			fila2 = True
			return fila2
	#retorna el documento en una sola linea
	return fila2

#toma la linea del documento y verifica que solo contenga puntos y equis
def validacion(archivoEnUnaLinea):
	check = True
	error = False
	fallo = 'Archivo incorrecto'
	errorFila = 'El largo de alguna(s) fila(s) no corresponde(n) al requerido, modifique el archivo'
	errorCaracter = "algun(os) caracter(es) no corresponde(n) a lo solicitado, modifique el archivo"
	mensaje = ""

	if (archivoEnUnaLinea == True):
		mensaje = ""
		mensaje += "\n" + fallo + "\n" + errorFila
		check = False
		return mensaje
	else:
		for conjunto in archivoEnUnaLinea:
			for letra in conjunto:
				if not((letra == ".")or(letra == "x")):
					error = True
	if error:
		mensaje = ""
		mensaje += "\n" + fallo + "\n" + errorCaracter
		return mensaje
	#si no contiene ningun error devuelve true, en caso de tener un error devuelve el tipo de error
	return check


#_____________________________________________________________________________________________________________________________________________________________#

#FUNCIONES QUE TRANSFORMAN DE ASCII A UN NUMERO ENTERO

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

#Transforma el string fila[i] en una fila de "n" elementos (con n como el largo del string de fila[i])
def separarCaracteres(archivoEnUnaLinea):
	caracter = []
	for i in range(7):
		caracter.append([])
		caracter[i] = list(archivoEnUnaLinea[i])
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
	indiceOperacion = None
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

#_____________________________________________________________________________________________________________________________________________________________#

#FUNCION QUE SE ENCARGA DE CALCULAR LOS NUMEROS

#Transforma los numeros a enteros y los opera
def calculadora(enteroNumero, indiceOperacion, tipoOperacion):
	numeroSt1 = ''
	numeroSt2 = ''
	error = False
	resultadoOperacion = ""
	primero = ""
	segundo = ""
	
	if indiceOperacion != None:
		for i in range(indiceOperacion):
			numeroSt1 = numeroSt1 + enteroNumero[i]
		primero = int(numeroSt1)
		for i in range(indiceOperacion+1, len(enteroNumero)):
			numeroSt2 = numeroSt2 + enteroNumero[i]
		segundo = int(numeroSt2)
	else:
		for i in range(len(enteroNumero)):
			numeroSt1 = numeroSt1 + enteroNumero[i]
		primero = int(numeroSt1)
		segundo = 0
	if tipoOperacion == '+':
		resultadoOperacion = primero + segundo
	elif tipoOperacion == '-':
		resultadoOperacion = primero - segundo
	elif tipoOperacion == '*':
		resultadoOperacion = primero * segundo
	elif tipoOperacion == '/':
		if segundo != 0:
			resultadoOperacion = round((float(primero) / float(segundo)),4)
		else:
			resultadoOperacion = "No se puede dividir por CERO"
	if (resultadoOperacion != "No se puede dividir por CERO"):
		if (resultadoOperacion - int(resultadoOperacion)) == 0:
			resultadoOperacion = int(resultadoOperacion)
	return resultadoOperacion

#_____________________________________________________________________________________________________________________________________________________________#

#FUNCIONES QUE SE ENCARGAN DE PASAR EL NUMERO A ASCII

#Transforma el resultado en una lista de numeros ASCII
def reconvertir(resultado):
	listaAscii = []
	resultadoString = list(str(resultado))
	for i in range(len(resultadoString)):
		for j in range(len(STR)):
			if resultadoString[i] == STR[j]:
				listaAscii.append(ASCII[j])	
	return listaAscii

#La lista de numeros ASCII se transforma en una lista con las 7 filas del resultado final
def reordenar(resultadoAscii):
	resultado = []
	resultado2 = []
	resultado3 = ''
	for i in range(7):				
		resultado.append([])
		for j in range(len(resultadoAscii)):
			resultado[i].append(resultadoAscii[j][i])
	for i in range(7):
		resultado2.append('')
		for j in range(len(resultado[i])):
			for k in range(5):
			       resultado2[i] = resultado2[i] + resultado[i][j][k]
			if j != len(resultado[i]):
				resultado2[i] = resultado2[i] + '.'
		resultado2[i] = resultado2[i][0:len(resultado2[i])-1]
	for i in range(7):
		resultado3 = resultado3 + resultado2[i] + '\n'
	return resultado3

#_____________________________________________________________________________________________________________________________________________________________#


#SE JUNTARON las constantes para poder cambiarlas facilmente en un futuro
notFound = "NO se ha encontrado el archivo, por favor intente nuevamente"
notMatch = "el archivo no coincide con nada almacenado \n este error probablemente se deba a un caracter mal ubicado"
linea = "_________________________________________________________________________\n"
O = 'OPERACION\n'
R = 'RESULTADO\n'
fallo = 'Archivo incorrecto'
errorFila = 'El largo de alguna(s) fila(s) no corresponde(n) al requerido, modifique el archivo'
errorCaracter = "algun(os) caracter(es) no corresponde(n) a lo solicitado, modifique el archivo"

#_____________________________________________________________________________________________________________________________________________________________#

#FUNCION PRINCIPAL DEL PROGRAMA
def main(event):
	try:
		nombreArchivo = box.get()
		archivoEnUnaLinea = leerArchivo(nombreArchivo)
		try:
			#en ves de crear un for para que cree la matriz, se coloca asi para ahorrar espacio
			matrizInicial = archivoEnUnaLinea[0]+"\n"+archivoEnUnaLinea[1]+"\n"+archivoEnUnaLinea[2]+"\n"+archivoEnUnaLinea[3]+"\n"+archivoEnUnaLinea[4]+"\n"+archivoEnUnaLinea[5]+"\n"+archivoEnUnaLinea[6]+"\n"
		except Exception as e:
			#si da algun error no entregara la matriz, por lo que entregamos un texto vacio
			matrizInicial = ""
		if (validacion(archivoEnUnaLinea) == True):
			#el archivo no contiene ningun error
			#_________________ASCII_A_NUMERO________________#
			caracter = separarCaracteres(archivoEnUnaLinea)
			numero = agruparCaracteres(caracter)
			enteroMatriz = agruparNumeros(numero,caracter)
			enteroNumero = reemplazar(enteroMatriz)
			indiceOperacion = posicionOperador(enteroNumero)
			tipoOperacion = operacion(enteroNumero)
			resultadoOperacion = calculadora(enteroNumero,indiceOperacion,tipoOperacion)
			#______________OPERACION_EN_TERMINAL____________#
			print (linea+O+linea)
			print matrizInicial
			print (linea+R+linea)
			#__________________NUMERO_A_ASCII_______________#
			numeroEnArreglo = reconvertir(resultadoOperacion)
			matrizResultado = reordenar(numeroEnArreglo)       
			#____________OPERACION_EN_INTERFAZ______________#
			Operation.config(text=(linea+O+linea))
			Matriz.config(text=matrizInicial)
			Result.config(text=(linea+R+linea))
			#_______________________________________________#
			if (resultadoOperacion == "No se puede dividir por CERO"):
				#mostrar en interfaz "no se puede dividir por CERO"
				OUTPUT.config(text=resultadoOperacion)
				#mostrar en terminal "no se puede dividir por CERO"
				print resultadoOperacion
			else:
				#mostrar matriz final en interfaz
				OUTPUT.config(text=matrizResultado)
				#mostrar matriz final en terminal
				print matrizResultado
		else:
			#si la validacion fallo, existen dos tipos de error
			#error de fila, cuando una o varias son mas largas que las otras
			if (validacion(archivoEnUnaLinea) == ("\n" + fallo + "\n" + errorFila)):
				#abre una ventana aparte que muestra el error y vacia todos los demas textos en pantalla
				tkMessageBox.showwarning("warning", (validacion(archivoEnUnaLinea)))
				Operation.config(text="")
				Result.config(text="")
				OUTPUT.config(text="")
				Matriz.config(text="")
			elif (validacion(archivoEnUnaLinea) == ("\n" + fallo + "\n" + errorCaracter)):
				#error de caracter, en caso de que haya un caracter que no coincida con un punto o una equis
				#abre una ventana aparte que muestra el error y vacia todos los demas textos en pantalla
				tkMessageBox.showwarning("warning", (validacion(archivoEnUnaLinea)))
				message.config(text="")
				Operation.config(text="")
				Result.config(text="")
				OUTPUT.config(text="")
				Matriz.config(text="")
			print validacion(archivoEnUnaLinea)
			print archivoEnUnaLinea
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
		tkMessageBox.showwarning("warning", fallo+"\n"+notMatch)
		#vacia todos los textos en pantalla
		message.config(text="")
		Operation.config(text="")
		Result.config(text="")
		OUTPUT.config(text="")
		Matriz.config(text="")

#_____________________________________________________________________________________________________________________________________________________________#

#esta funcion se ejecuta cuando el usuario presiona el boton de ayuda, muestra la ventana ayuda
def instrucciones():
	instrucciones1 = "-ingresa el nombre del archivo en la caja de texto. \nEl archivo debe contener reglas basicas en formato ASCII para ser leido\n"
	instrucciones2 = "se realizara el proceso matematico correspondiente \nse mostrara en pantalla el resultado obtenido"
	tkMessageBox.showinfo("instrucciones", instrucciones1+instrucciones2)

#_____________________________________________________________________________________________________________________________________________________________#

#ESTA FUNCION ES UNA COPIA EXACTA AL MAIN PERO ESTA PROGRAMADA PARA QUE LA USE EL BUSCADOR DE ARCHIVOS GRAFICO
#la otra no se puede usar con  un argumento dado ya que contiene el argumento event que permite asignar teclas a diferentes funciones

def buscar(nombreArchivo):
	try:
		archivoEnUnaLinea = leerArchivo(nombreArchivo)
		try:
			#en ves de crear un for para que cree la matriz, se coloca asi para ahorrar espacio
			matrizInicial = archivoEnUnaLinea[0]+"\n"+archivoEnUnaLinea[1]+"\n"+archivoEnUnaLinea[2]+"\n"+archivoEnUnaLinea[3]+"\n"+archivoEnUnaLinea[4]+"\n"+archivoEnUnaLinea[5]+"\n"+archivoEnUnaLinea[6]+"\n"
		except Exception as e:
			#si da algun error no entregara la matriz, por lo que entregamos un texto vacio
			matrizInicial = ""
		if (validacion(archivoEnUnaLinea) == True):
			#el archivo no contiene ningun error
			#_________________ASCII_A_NUMERO________________#
			caracter = separarCaracteres(archivoEnUnaLinea)
			numero = agruparCaracteres(caracter)
			enteroMatriz = agruparNumeros(numero,caracter)
			enteroNumero = reemplazar(enteroMatriz)
			indiceOperacion = posicionOperador(enteroNumero)
			tipoOperacion = operacion(enteroNumero)
			resultadoOperacion = calculadora(enteroNumero,indiceOperacion,tipoOperacion)
			#______________OPERACION_EN_TERMINAL____________#
			print (linea+O+linea)
			print matrizInicial
			print (linea+R+linea)
			#__________________NUMERO_A_ASCII_______________#
			numeroEnArreglo = reconvertir(resultadoOperacion)
			matrizResultado = reordenar(numeroEnArreglo)
			#____________OPERACION_EN_INTERFAZ______________#
			Operation.config(text=(linea+O+linea))
			Matriz.config(text=matrizInicial)
			Result.config(text=(linea+R+linea))
			#_______________________________________________#
			if (resultadoOperacion == "No se puede dividir por CERO"):
				#mostrar en interfaz "no se puede dividir por CERO"
				OUTPUT.config(text=resultadoOperacion)
				#mostrar en terminal "no se puede dividir por CERO"
				print resultadoOperacion
			else:
				#mostrar matriz final en interfaz
				OUTPUT.config(text=matrizResultado)
				#mostrar matriz final en terminal
				print matrizResultado
		else:
			#si la validacion fallo, existen dos tipos de error
			#error de fila, cuando una o varias son mas largas que las otras
			if (validacion(archivoEnUnaLinea) == ("\n" + fallo + "\n" + errorFila)):
				#abre una ventana aparte que muestra el error y vacia todos los demas textos en pantalla
				tkMessageBox.showwarning("warning", (validacion(archivoEnUnaLinea)))
				Operation.config(text="")
				Result.config(text="")
				OUTPUT.config(text="")
				Matriz.config(text="")
			elif (validacion(archivoEnUnaLinea) == ("\n" + fallo + "\n" + errorCaracter)):
				#error de caracter, en caso de que haya un caracter que no coincida con un punto o una equis
				#abre una ventana aparte que muestra el error y vacia todos los demas textos en pantalla
				tkMessageBox.showwarning("warning", (validacion(archivoEnUnaLinea)))
				message.config(text="")
				Operation.config(text="")
				Result.config(text="")
				OUTPUT.config(text="")
				Matriz.config(text="")
			print validacion(archivoEnUnaLinea)
			print archivoEnUnaLinea
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
		tkMessageBox.showwarning("warning", fallo+"\n"+notMatch)
		#vacia todos los textos en pantalla
		message.config(text="")
		Operation.config(text="")
		Result.config(text="")
		OUTPUT.config(text="")
		Matriz.config(text="")

def searchFile():
	archivo=askopenfile()
	buscar(archivo.name)
	box.insert(0, archivo.name)


#_____________________________________________________________________________________________________________________________________________________________#

#INTERFAZ GRAFICA

#primero se crea la variable de mi ventana principal llamada root
root = Tk()
#le agrego un titulo a mi ventana
root.title("Calculadora ASCII")
#luego asigno la tecla ENTER para que ejecute la funcion main y haga el papel del boton buscar
root.bind("<Return>", main)
# en Sistemas Operativos de linux no permite cambiar el icono de la ventana por lo que podemos saber que S.O. se trata
# intenta abrir el programa en linux se le mostrara un mensaje explicandole el fallo y recomendandole abrirlo en windows
try:
	ubuntu = False
	root.iconbitmap('icon.ico')
except Exception as e:
	ubuntu = True
	tkMessageBox.showinfo("linux detectado", "debido a que usas una distro de linux nos es imposible cambiar\nel icono de la ventana, para una proxima ves en windows funcionara mucho mejor")

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
submitFile = Button(leftFrame, text="Buscar", fg="black", command=searchFile)
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
status = Label(root, text="Version 2.5.1 - Calculadora ASCII", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()
#_____________________________________________________________________________________________________________________________________________________________#
