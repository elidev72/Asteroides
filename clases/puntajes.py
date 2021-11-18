class Puntajes:
	def __init__(self, nombre_Jugador, puntaje, nivel):
		self.nombre_Jugador = nombre_Jugador
		self.puntaje = puntaje
		self.nivel = nivel

	def getDatosJugador(self):
		return self.nombre_Jugador + " - " + str(self.puntaje) + " - " + str(self.nivel)

	def getNombreJugador(self):
		return self.nombre_Jugador

	def getPuntaje(self):
		return self.puntaje

	def getNivel(self):
		return self.nivel