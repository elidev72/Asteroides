import pygame, sys
from pygame.locals import *

#Pausar el programa, permite controlar los FPS
clock = pygame.time.Clock()

#Constantes
NOMBRE_JUEGO = "Asteroides 1.0"
FUENTE = "Comic Sans MS"
FPS = 240
BLANCO = (255,255,255)

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
    #Esto controla los FP por segundo
    clock.tick(FPS)
#------------------------------------------------Fin funcion------------------------------------------------

#----------------------------------------------Inicio funcion-----------------------------------------------
"""
    PRE:
    POST:
"""
def menu(ventana, ancho, alto):
    color_botones = (255, 0, 0)

    #Imagen de fondo:
    ventana.blit(pygame.image.load("imagenes/espacio.png"),(0,0))

    mostrarTextoEnPantalla(ventana, NOMBRE_JUEGO, FUENTE, 60, (159,249,174), ancho/2 - 200, alto/12)

    mostrarTextoEnPantalla(ventana, "Opciones del juego", FUENTE, 40, BLANCO, ancho/2 - 175, alto/3)


    menu = True
    while menu:

        #Coordenadas y tamanio de los botones.
        boton1 = pygame.Rect(200, 350, 600, 50)
        boton2 = pygame.Rect(200, 450, 600, 50)
        boton3 = pygame.Rect(200, 550, 600, 50)

        #Coloco los votones en pantalla
        pygame.draw.rect(ventana, color_botones, boton1)
        mostrarTextoEnPantalla(ventana, "Jugar", FUENTE, 30, BLANCO, 465, 350)
        pygame.draw.rect(ventana, color_botones, boton2)
        mostrarTextoEnPantalla(ventana, "Comandos del juego", FUENTE, 30, BLANCO, 380, 450)
        pygame.draw.rect(ventana, color_botones, boton3)
        mostrarTextoEnPantalla(ventana, "TOP 10 Puntajes", FUENTE, 30, BLANCO, 390, 550)

        #Para capturar los eventos que van sucediendo
        for evento in pygame.event.get():
            #Para que cierre al precionar la cruz de la ventana.
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Para que cierre al precionar la tecla escape.
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                #Posicion del mouse
                mouse_Posicion = pygame.mouse.get_pos()
                if boton1.collidepoint(mouse_Posicion):
                    menu = False

        pygame.display.update()
        #Esto controla los FP por segundo
        clock.tick(FPS)
#------------------------------------------------Fin funcion------------------------------------------------

#----------------------------------------------Inicio funcion-----------------------------------------------
"""
    PRE:
    POST:
"""
def game():
    pass
#------------------------------------------------Fin funcion------------------------------------------------

#----------------------------------------------Inicio funcion-----------------------------------------------
"""
    PRE:
    POST:
"""
def options():
    pass
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
    mostrarTextoEnPantalla(ventana, "Juego en pausa, presione C para seguir jugando", FUENTE, 40, BLANCO, cordenada_X, cordenada_Y)

    while pausado:
                    
        #Para capturar los eventos que van sucediendo
        for evento in pygame.event.get():
            #Para que cierre al precionar la cruz de la ventana.
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Para que cierre al precionar la tecla escape.
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            #Para que el juego salga de la pausa.
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_c:
                    pausado = False
#------------------------------------------------Fin funcion------------------------------------------------

#----------------------------------------------Inicio funcion-----------------------------------------------
"""
    PRE:
    POST:
"""
#------------------------------------------------Fin funcion------------------------------------------------