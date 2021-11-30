class Puntajes:
	"""
	    PRE: El Puntaje no debe haber sido creado, y debe existir, el nombre_Jugador, y el puntaje y nivel (estos
	    2 ultimos deben ser de tipo int).
	    POST: El Puntaje queda creado.
	"""
	def __init__(self, nombre_Jugador, puntaje, nivel):
		self.nombre_Jugador = nombre_Jugador
		self.puntaje = puntaje
		self.nivel = nivel

#---------------------------------------------------Metodos-------------------------------------------------

#-----------------------------------------------Inicio metodo-----------------------------------------------
	"""
	    PRE: El Puntaje debe haber sido creado.
	    POST: Devuelvo los datos del puntaje con el formato para mostrar en pantalla.
	"""
	def getDatosJugador(self):
		return self.nombre_Jugador + " - " + str(self.puntaje) + " - " + str(self.nivel)
#-------------------------------------------------Fin metodo------------------------------------------------