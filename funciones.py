import pygame, sys
from pygame.locals import *
from tkinter import *
from clases import puntajes
from clases import Asteroide
from random import randint #generar numeros aleatorios
from io import open #archivos

#Pausar el programa, permite controlar los FPS
clock = pygame.time.Clock()

#Constantes
NOMBRE_JUEGO = "Asteroides 1.0"
FUENTE = "Comic Sans MS"
FPS = 60
BLANCO = (255,255,255)

#Listas:
lista_Asteroide = []

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
def listaDeTop10Puntajes(nombre_Archivo_Puntajes):
    archivo = open(nombre_Archivo_Puntajes, "r")
    lista = archivo.readlines()
    archivo.close()
    lPuntajes = []

    for i in range(len(lista)):
        cadena  = lista[i]
        nombre  = cadena[:cadena.index(',')]
        cadena  = cadena[cadena.index(',')+1:]
        puntaje = cadena[:cadena.index(',')]
        cadena  = cadena[cadena.index(',')+1:]
        nivel   = cadena[:cadena.index(";")]
        dato    = puntajes.Puntajes(nombre, int(puntaje), int(nivel))
        lPuntajes.append(dato)

    return lPuntajes
#------------------------------------------------Fin funcion------------------------------------------------

#----------------------------------------------Inicio funcion-----------------------------------------------
"""
    PRE:
    POST:
"""
def mostrarTop10Puntajes(ventana, ancho, alto, nombre_Archivo_Puntajes, color_Boton):
    lPuntajes = listaDeTop10Puntajes(nombre_Archivo_Puntajes)

    #Imagen de fondo:
    ventana.blit(pygame.image.load("imagenes/espacio.png"),(0,0))
    mostrarTextoEnPantalla(ventana, "TOP 10 Puntajes", FUENTE, 40, BLANCO, ancho/2-150, 0)
    mostrarTextoEnPantalla(ventana, "Posicion - Jugador  -  Punjate - Nivel", FUENTE, 40, BLANCO, ancho/2-350, 100)
    
    #Datos jugadores
    for i in range(len(lPuntajes)):
        mostrarTextoEnPantalla(ventana,"#" + str(i+1) + " - " + lPuntajes[i].getDatosJugador(), FUENTE, 25, (255,51,51), 375, 175+50*i)
    
    del i

    #Coordenadas y tamanio de los botones.
    boton_Salir = pygame.Rect(20, 690, 200, 50)
    #Coloco los votones en pantalla
    pygame.draw.rect(ventana, color_Boton, boton_Salir)
    mostrarTextoEnPantalla(ventana, "<- Volver", FUENTE, 30, BLANCO, 60, 692)

    mostrar_Puntajes = True
    while mostrar_Puntajes:

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
                if boton_Salir.collidepoint(mouse_Posicion):
                    mostrar_Puntajes = False

        pygame.display.update()
        #Esto controla los FP por segundo
        clock.tick(FPS)
#------------------------------------------------Fin funcion------------------------------------------------

#----------------------------------------------Inicio funcion-----------------------------------------------
"""
    PRE:
    POST:
"""
def menu(ventana, ancho, alto, nombre_Archivo_Puntajes):
    color_botones = (255, 0, 0)

    #Esta variable es para que no se actualice a cada instante el menu y solo lo haga cuando debe.
    actualizar = True

    #Inicio bucle de la funcion
    menu = True
    while menu:

        if actualizar == True:
            actualizar = False
            #Imagen de fondo:
            ventana.blit(pygame.image.load("imagenes/espacio.png"),(0,0))

            mostrarTextoEnPantalla(ventana, NOMBRE_JUEGO, FUENTE, 120, (159,249,174), ancho/10, alto/12)

            mostrarTextoEnPantalla(ventana, "Opciones del juego", FUENTE, 40, BLANCO, ancho/2 - 175, alto/3)

            #Coordenadas y tamanio de los botones.
            boton1 = pygame.Rect(200, 350, 600, 50)
            boton2 = pygame.Rect(200, 450, 600, 50)
            boton3 = pygame.Rect(200, 550, 600, 50)

            #Coloco los votones en pantalla
            pygame.draw.rect(ventana, color_botones, boton1)
            mostrarTextoEnPantalla(ventana, "Jugar", FUENTE, 30, BLANCO, 465, 350)
            pygame.draw.rect(ventana, color_botones, boton2)
            mostrarTextoEnPantalla(ventana, "Comandos del juego", FUENTE, 30, BLANCO, 375, 450)
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
                elif boton3.collidepoint(mouse_Posicion):
                    mostrarTop10Puntajes(ventana, ancho, alto, nombre_Archivo_Puntajes, color_botones)
                    actualizar = True
                    
        
        pygame.display.update()
        #Esto controla los FP por segundo
        clock.tick(FPS)
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
def barraDeHP(ventana, x, y, vida, maxHP):
    Color = (0, 255, 0)
    BAR_LENGHT = 180
    BAR_HEIGHT = 40
    fill = (vida / 100) * BAR_LENGHT
    borde = pygame.Rect(x, y, BAR_LENGHT, BAR_HEIGHT)
    fill = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(ventana, Color, fill)
    pygame.draw.rect(ventana, BLANCO, borde, 2)
    mostrarTextoEnPantalla(ventana, str(vida) + str("/") + str(maxHP), FUENTE, 20, (204,0,0), 60, 10)
    
#------------------------------------------------Fin funcion------------------------------------------------

#----------------------------------------------Inicio funcion-----------------------------------------------
"""
    PRE:
    POST:
"""
def ingresarNombre():
    raiz = Tk()

    #StringVar:
    nombre = StringVar()

    raiz.title("Nombre de jugador")
    raiz.resizable(False, False)
    raiz.geometry("400x100")
    raiz.config(bg="#36FFF9")

    #Etiqueta:
    texto = Label(raiz, text="Ingrese su nombre: ", bg="#14FCB6")
    texto.place(x = 10, y = 10)
    #Caja de texto:
    caja = Entry(raiz, textvariable=nombre)
    caja.place(x = 150, y = 40)

    raiz.mainloop() #Siempre debe ir al final

    return nombre
#------------------------------------------------Fin funcion------------------------------------------------

#----------------------------------------------Inicio funcion-----------------------------------------------
"""
    PRE:
    POST:
"""
def finDeLaPartida(ventana, pts, nivel, ancho, alto, nombre_Archivo_Puntajes):
    lPuntajes = listaDeTop10Puntajes(nombre_Archivo_Puntajes)

    ventana.blit(pygame.image.load("imagenes/espacio.png"),(0,0))
    mostrarTextoEnPantalla(ventana, "FIN DEL JUEGO", FUENTE, 80, (159,249,174), ancho/10, alto/12)


    puntaje_Top = False
    contador = 0
    while (not puntaje_Top) and (contador < 10):
        if pts > lPuntajes[contador].puntaje:
            puntaje_Top = True
            contador += 1

    if puntaje_Top:
        mostrarTextoEnPantalla(ventana, "Puntaje top logrado!", FUENTE, 50, (159,249,174), ancho/10, alto/2)


    #Coordenadas y tamanio de los botones.
    boton_Salir = pygame.Rect(20, 690, 200, 50)
    #Coloco los votones en pantalla
    pygame.draw.rect(ventana, (255, 0, 0), boton_Salir)
    mostrarTextoEnPantalla(ventana, "<- Volver", FUENTE, 30, BLANCO, 60, 692)

    #Ingresar puntaje top:
    if puntaje_Top:
        nombre = ingresarNombre()

        dato = puntajes.Puntajes(nombre.get(), pts, nivel)
        lPuntajes.insert(contador-1, dato)

    archivo = open(nombre_Archivo_Puntajes, "r+")
    for i in range(10):
        sTexto = lPuntajes[i].nombre_Jugador + "," + str(lPuntajes[i].puntaje) + "," + str(lPuntajes[i].nivel) + ";\n"
        archivo.write(sTexto)
    archivo.close()

    end = True
    while end:

        #Para capturar los eventos que van sucediendo
        evento = pygame.event.get()
        for accion in evento:
            #Para que cierre al precionar la cruz de la ventana.
            if accion.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            #Para que cierre al precionar la tecla escape.
            if accion.type == pygame.KEYDOWN:
                if accion.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if accion.type == pygame.MOUSEBUTTONDOWN:
                #Posicion del mouse
                mouse_Posicion = pygame.mouse.get_pos()
                if boton_Salir.collidepoint(mouse_Posicion):
                    end = False

        pygame.display.update()
        #Esto controla los FP por segundo
        clock.tick(FPS)

#------------------------------------------------Fin funcion------------------------------------------------

#----------------------------------------------Inicio funcion-----------------------------------------------
"""
    PRE:
    POST:
"""
#------------------------------------------------Fin funcion------------------------------------------------
