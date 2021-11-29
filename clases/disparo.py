import pygame

class Disparo(pygame.sprite.Sprite):
	def __init__(self, posX, posY):
		pygame.sprite.Sprite.__init__(self)
		self.imagenDisparo = pygame.image.load("imagenes/laser1.png")
		self.rect = self.imagenDisparo.get_rect()
		self.velocidad_Disparo = 10
		self.rect.top = posY
		self.rect.left = posX

	def recorrido(self):
		self.rect.top -= self.velocidad_Disparo

	def dibujar(self, superficie):
		superficie.blit(self.imagenDisparo, self.rect)