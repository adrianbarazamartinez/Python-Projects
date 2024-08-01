'''
Reproduce el clásico juego de arcade Pong. Para ello puedes usar el módulo "turtle" para
crear los componentes del juego y detectar las colisiones de la pelota con las paletas de los
jugadores.También puedes definir una serie de asignaciones de teclas para establecer los
controles del usuario para las paletas de los jugadores izquierda y derecha.
'''
#importamos el modulo turtle 
import turtle

#Funciones
def jugadorA_up():
    '''En esta funcion enviaremos la pala del jugador A y aumentaremos su y 20 pixeles para que ascienda y la guardaremos su nueva coordenada y'''
    y = jugadorA.ycor()
    y += 20
    jugadorA.sety(y)

def jugadorA_down():
    '''En esta funcion enviaremos la pala del jugador A y disminuiremos su y 20 pixeles para que descienda y la guardaremos su nueva coordenada y'''
    y = jugadorA.ycor()
    y -= 20
    jugadorA.sety(y)

def jugadorB_up():
    '''En esta funcion enviaremos la pala del jugador B y aumentaremos su y 20 pixeles para que ascienda y la guardaremos su nueva coordenada y'''
    y = jugadorB.ycor()
    y += 20
    jugadorB.sety(y)

def jugadorB_down():
    '''En esta funcion enviaremos la pala del jugador B y disminuiremos su y 20 pixeles para que descienda y la guardaremos su nueva coordenada y'''
    y = jugadorB.ycor()
    y -= 20
    jugadorB.sety(y)

def colision_bordes_pelota(pelota):
    '''En esta funcion le pasaremos el objeto pelota y si supera los bordes sup e inf cambia el incremento en y a negativo, y si los supera en x empieza en 0 y cambia el sentido de x'''
    #Bordes sup e inferior
    if pelota.ycor() > 390:
        pelota.movy = -pelota.movy
    if pelota.ycor() < -390:
        pelota.movy = -pelota.movy
    #Bordes derecha e izquierda
    if pelota.xcor() > 490:
        pelota.setposition(0,0)
        pelota.movx = - pelota.movx
        #sumamos un punto al jugador A y borramos el marcador y lo reescribimos actualizado
        jugadorA.puntos +=1
        marcador.clear()
        marcador.goto(-350,350)
        marcador.write('Jugador A:  '+str(jugadorA.puntos),align = 'left', font =('Arial',20,'normal'))
        marcador.goto(150,350)
        marcador.write('Jugador B:  '+str(jugadorB.puntos),align = 'left', font =('Arial',20,'normal'))
    if pelota.xcor() < -490:
        pelota.setposition(0,0)
        pelota.movx = - pelota.movx
        #sumamos un punto al jugador B y borramos el marcador y lo reescribimos actualizado
        jugadorB.puntos +=1
        marcador.clear()
        marcador.goto(-350,350)
        marcador.write('Jugador A:  '+str(jugadorA.puntos),align = 'left', font =('Arial',20,'normal'))
        marcador.goto(150,350)
        marcador.write('Jugador B:  '+str(jugadorB.puntos),align = 'left', font =('Arial',20,'normal'))

def colision_palas_pelota(pelota,jugadorA,jugadorB):
    '''En esta funcion le pasaremos los objeto pelota, jugador A y jugador B Y comnprobará las colisiones'''
    #colision con la pala de la derecha
    if (pelota.xcor() > 440 and pelota.xcor() < 450) and ( pelota.ycor() < jugadorB.ycor()+70) and(pelota.ycor()>jugadorB.ycor()-70):
        pelota.movx = -pelota.movx
    #colision con la pala izquierda 
    if (pelota.xcor() < -440 and pelota.xcor() > -450) and ( pelota.ycor() < jugadorA.ycor()+70) and(pelota.ycor()>jugadorA.ycor()-70):
        pelota.movx = -pelota.movx






#creamos un objeto tipo Screen
ventana = turtle.Screen()
ventana.title('Juego Pong')
ventana.bgcolor('black')
ventana.setup(width= 1000, height = 800) 
ventana.tracer(0) #activa la animacion de los objetos dentro de la ventana

#creamos los objetos del juego tipo Turtle 
#jugadorA (LA PALA DEL JUGADOR A)
jugadorA = turtle.Turtle()
jugadorA.speed(0) #copmando para que se mueva el objeto  el 0 es para que aparezca el cuadrado 
jugadorA.shape('square') #el cuadrado por delfault es de 10x10 pixels
jugadorA.color('white')
jugadorA.penup() #levanta el pen para que no dibuje la linea de desplazamiento del cuadrado
jugadorA.goto(-450,0) #lo movemos al lado izquierdo de la ventana
jugadorA.shapesize(stretch_wid= 7,stretch_len= 1) #aumentamos el tamaño del cuadrado creado
jugadorA.puntos = 0 #iniciamos los puntos del jugador A a 0

#jugadorB (LA PALA DEL JUGADOR B)
jugadorB = turtle.Turtle()
jugadorB.speed(0) 
jugadorB.shape('square') 
jugadorB.color('white')
jugadorB.penup() 
jugadorB.goto(450,0) #lo movemos al lado derecho de la ventana
jugadorB.shapesize(stretch_wid= 7,stretch_len= 1)
jugadorB.puntos = 0 #iniciamos los puntos del jugador B a 0

#pelota
pelota = turtle.Turtle()
pelota.speed(0) 
pelota.shape('circle') 
pelota.color('white')
pelota.penup() 
pelota.goto(0,0)
pelota.shapesize(stretch_wid= 2) #en un circulo solo modificamos uno 
pelota.movx = 1 # esto es una variable para hacer un incremento de 1 pix en eje x
pelota.movy = 1 #esto es una variable para hacer un incremento de 1 pix en eje y

#la linea divisoria del centro del campo (No ponemos pen up ni speed porque la idea es dejar el lapiz para crear la linea)
linea_divisoria = turtle.Turtle()
linea_divisoria.color('white')
linea_divisoria.goto(0,500)
linea_divisoria.goto(0,-500)

#Marcador
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color('white')
marcador.penup()
marcador.hideturtle()
marcador.goto(-350,350)
marcador.write('Jugador A:  '+str(jugadorA.puntos),align = 'left', font =('Arial',20,'normal'))
marcador.goto(150,350)
marcador.write('Jugador B:  '+str(jugadorB.puntos),align = 'left', font =('Arial',20,'normal'))


#teclado
ventana.listen()#aqui le decimos que la pantalla lea por teclado, y que escuche los eventos, establecemos el foco en la screen
ventana.onkeypress(jugadorA_up,'w') #es un evento ligado a una tecla,aqui le tenemos que pasar una funcion sin argumentos seguido del string que se introducirá por teclado para hacer la funcion
ventana.onkeypress(jugadorA_down,'s')
ventana.onkeypress(jugadorB_up,'Up') # Up es la felcha hacia arriba
ventana.onkeypress(jugadorB_down,'Down') #Down es la flecha hacia abajo

#Main del programa
seguir = True
while seguir == True:
    ventana.update()
    #aqui le damos movimiento inicial a la pelota incrementandola en x e y
    pelota.setx(pelota.xcor()+pelota.movx)
    pelota.sety(pelota.ycor()+pelota.movy)
    #Colisiones
    colision_bordes_pelota(pelota)
    colision_palas_pelota(pelota,jugadorA,jugadorB)
    #comprobamos que si jugador AS o B llegan a 5 puntos se termina el juego
    if jugadorA.puntos == 5:
        ventana.clearscreen()
        ventana.bgcolor('black')
        marcador.goto(0,0)
        marcador.write('GANADOR JUGADOR A',align = 'center', font =('Arial',40,'normal'))
        seguir = False
    elif jugadorB.puntos == 5:
        ventana.clearscreen()
        ventana.bgcolor('black')
        marcador.goto(0,0)
        marcador.write('GANADOR JUGADOR B',align = 'center', font =('Arial',40,'normal'))
        seguir = False

#para evitar cierre automatico
turtle.done()
