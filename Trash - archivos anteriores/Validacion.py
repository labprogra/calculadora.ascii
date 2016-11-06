#Ejemplo funcion validacion (caracteres)
NUM0 = [['x','x','x','x','x'],['x','.','.','.','x'],['x','.','.','.','x'],['o','.','.','.','x'],['x','.','.','.','x'],['x','.','.','.','x'],['x','x','x','x','x']]
a = True
b = NUM0

for i in NUM0:
     for j in i:
         if ((j != "x") and (j != ".")):
            print j



print ("Archivo bien ingresado")
            
