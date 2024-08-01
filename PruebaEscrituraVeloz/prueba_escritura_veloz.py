import tkinter
import sentences
import time
#definimos algunas funciones
tiempo_inicial=0.0
tiempo_final=0.0
tiempo_total=0.0

def start_time():
     global tiempo_inicial
     tiempo=time.time()
     tiempo_inicial=tiempo
     print(tiempo_inicial) 
def end_time():
     global tiempo_final
     tiempo=time.time()
     tiempo_final=tiempo
     print(tiempo_final) 

def actualizar_tiempo():
          global tiempo_total,tiempo_inicial,tiempo_final
          tiempo_total=tiempo_final-tiempo_inicial
          etiqueta_Tiempo['text']='Tiempo: '+str(tiempo_total)+' segundos'

def corregir_frase():
    if cajaTexto.get()==etiqueta2['text']:
          etiqueta3['text']='Resultado: Respuesta correcta'
    else:
         etiqueta3['text']='Resultado: Respuesta incorrecta'

       
      

#creamos la ventana principal
ventana = tkinter.Tk()
ventana.geometry("1000x700")

#creamos una etiqueta para la ventana
etiqueta1 = tkinter.Label(ventana, text='PRUEBA ESCRITURA VELOZ',bg='green')
etiqueta1.pack(fill=tkinter.X)

etiqueta2 = tkinter.Label(ventana, text= sentences.frases_al_azar(sentences.frases))
etiqueta2.pack()

#creamos los botones
boton1= tkinter.Button(ventana,text = 'Presiona para empezar el temporizador de 30 seg',command=start_time)
boton1.pack()


#creamos las cajas de texto
cajaTexto=tkinter.Entry(ventana)
cajaTexto.pack()

#creamos los botones
boton2= tkinter.Button(ventana,text = 'Presiona para enviar frase',command=end_time)
boton2.pack()


etiqueta_Tiempo = tkinter.Label(ventana, text= 'Tiempo:')
etiqueta_Tiempo.pack()
etiqueta3 = tkinter.Label(ventana, text= 'Resultado:')
etiqueta3.pack()
ventana.after(30000,actualizar_tiempo)
ventana.after(30000,corregir_frase)
# para que la ventana se corra siempre
ventana.mainloop()
