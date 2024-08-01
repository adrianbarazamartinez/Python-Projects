#importamos el modulo de tkinter
from tkinter import *
from tkinter import filedialog

#funciones 
def abrir_archivos():
    ruta_archivo= filedialog.askopenfilename(initialdir='D:\MasterFullStack\PREWORK\Modulo 5 - Python avanzado\Proyectos para desarrollar en Python\EditordeTexto', 
                                             filetypes=(('Text Files','*.txt'),('All Files','*.*')))
    with open(ruta_archivo) as archivo:
        contenido=archivo.read()
        texto.insert(END,contenido)   

def guardar_archivos():
    ruta_archivo= filedialog.asksaveasfilename(initialdir='D:\MasterFullStack\PREWORK\Modulo 5 - Python avanzado\Proyectos para desarrollar en Python\EditordeTexto',
                                               defaultextension='.txt', filetypes=[('Text Files','.txt'),('HTML Files','.html'),('All Files','.*')])
    texto_archivo=str(texto.get(1.0,END))
    with open(ruta_archivo,'w+') as archivo:
        archivo.write(texto_archivo) 



#creamos la ventana del editor
ventana= Tk()
ventana.title('EDITOR DE TEXTO')
ventana.geometry('800x800')
menu= Menu(ventana)
ventana.config(menu=menu)
menu_archivo=Menu(menu)
menu.add_cascade(label='Archivo',menu=menu_archivo)
menu_archivo.add_command(label='Abrir',command=abrir_archivos)
menu_archivo.add_command(label='Guardar',command=guardar_archivos)
menu.add_command(label='Salir',command=ventana.quit)

texto=Text(ventana,height=780,width=780)
texto.pack()

mainloop()