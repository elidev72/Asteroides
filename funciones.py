import pygame, sys
from pygame.locals import *

#----------------------------------------------Inicio funcion-----------------------------------------------
"""
    PRE: Debe existir la ventana donde se desea que se realice la funcion, la cordenada_X/Y y el
        tamanio_De_Letra deben ser valores de tipo numerico. tipo_De_Letra debe ser un string que indique
        la letra que desea utilizar para mostrar el mensaje y color debe ser un tupla que indique el color
        en formato RGB.
    POST: Se muestra por consola el mensaje ingresado en las coordenadas indicadas con el tipo de letra y
        y color señalado.
"""
def mostrarTextoEnPantalla(ventana, texto, tipo_De_Letra, tamanio_De_Letra, color, cordenada_X, cordenada_Y):
    #Preparacion fuente y texto:
    fuente = pygame.font.SysFont(tipo_De_Letra, tamanio_De_Letra)
    texto_Ventana = fuente.render(texto, True, color)
    #Mostrar texto:
    ventana.blit(texto_Ventana, (cordenada_X, cordenada_Y))
    pygame.display.update()
#------------------------------------------------Fin funcion------------------------------------------------

#----------------------------------------------Inicio funcion-----------------------------------------------
"""
    PRE: Debe existir la ventana donde se desea que se realice la funcion, la cordenada_X/Y deben ser valores
        de tipo numerico para mostrar que esta en pausa.
    POST: El juego queda en pausa mostrando el mensaje en las coordenadas indicadas hasta que se cierre la
        la consola o el usuario presione la tecla C para seguir jugando.
"""
def pause(ventana, cordenada_X, cordenada_Y):
    pausado = True

    #Mostrar que el juego esta en pausa
    mostrarTextoEnPantalla(ventana, "Juego en pausa, presione C para seguir jugando", "Arial", 40, ( 255, 255, 255), cordenada_X, cordenada_Y)

    while pausado:
                    
        #Para capturar los eventos que van sucediendo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pausado = False
#------------------------------------------------Fin funcion------------------------------------------------