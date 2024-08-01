#importamos modulos
from tkinter import *
from tkinter import messagebox
import datetime
import webbrowser
import random
import videos_youtube
#creamos las funciones
def activador_despertador():
    hora_entrada=str(hora_caja_Texto.get())
    min_entrada=str(min_caja_Texto.get())
    seg_entrada=str(seg_caja_Texto.get())
    if (0<len(hora_entrada)<=2 and 0<=int(hora_entrada)<=24) and (0<len(min_entrada)<=2 and 0<=int(min_entrada)<=60) and (0<len(seg_entrada)<=2 and 0<=int(seg_entrada)<=60) :
        resultado['text']='Despertador programado satisfactoriamente'
    else:
        resultado['text']='Error en la introduccion de la hora'


def video_aleatorio():
    hora_entrada=str(hora_caja_Texto.get())
    min_entrada=str(min_caja_Texto.get())
    seg_entrada=str(seg_caja_Texto.get())
    tiempo=str(datetime.datetime.now())
    hora=tiempo[11:13]
    min=tiempo[14:16]
    seg=tiempo[17:19]
    if resultado['text'] == 'Despertador programado satisfactoriamente':
        if hora==hora_entrada and min==min_entrada and seg==seg_entrada :
            video=random.choice(videos_youtube.youtube_urls)
            webbrowser.open(video)
            messagebox.showinfo(title='DESPERTADOR',message='DESPERTADOR ACTIVADO\nMUSICA SONANDO')

    ventana.after(100,video_aleatorio)
            
        


#creamos la ventana de inicio
ventana=Tk()
ventana.title('RELOJ DESPERTADOR YOUTUBE')
ventana.geometry('500x500')
titulo= Label(ventana,text='RELOJ DESPERTADOR YOUTUBE',font=32,background='red')
titulo.grid()
Hora=Label(ventana,text='RELOJ DESPERTADOR YOUTUBE',font=32)
hora_texto=Label(ventana,text='INTRODUCE LA HORA:',)
hora_texto.grid(row=1,column=0)
hora_caja_Texto=Entry(ventana)
hora_caja_Texto.grid(row=1,column=1)
min_texto=Label(ventana,text='INTRODUCE LOS MIN:',)
min_texto.grid(row=2,column=0)
min_caja_Texto=Entry(ventana)
min_caja_Texto.grid(row=2,column=1)
seg_texto=Label(ventana,text='INTRODUCE LOS SEG:',)
seg_texto.grid(row=3,column=0)
seg_caja_Texto=Entry(ventana)
seg_caja_Texto.grid(row=3,column=1)
hora_Introducida=Button(ventana,text='Enter',command= activador_despertador)
hora_Introducida.grid()
resultado=Label(ventana,text='Resultado:')
resultado.grid()
video_aleatorio()

mainloop()