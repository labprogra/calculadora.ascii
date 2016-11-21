from tkinter import *
import subprocess as sub
p = sub.Popen('./script',stdout=sub.PIPE,stderr=sub.PIPE)
output, errors = p.communicate()

root = Tk()
text = Text(root)
text.pack()
text.insert(END, output)
root.mainloop()

line = "_________________________________________________________________________\n"
				O = 'OPERACION\n'
				R = 'RESULTADO\n'
				Operation.config(text=(line+O+line))