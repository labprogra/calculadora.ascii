class Persona:
	def __init__(self, nombre):
		self.nombre = nombre
		self.edad = 20
		self.colorPelo = "negro"

	def hablar(self):
		return self.nombre

persona = Persona("danny")

mensaje = objeto.hablar()

print mensaje
