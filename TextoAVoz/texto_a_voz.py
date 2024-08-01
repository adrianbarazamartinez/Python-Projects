'''
La idea de este proyecto es convertir un artículo existente en un archivo de audio reproducible
en formato mp3. Para ello puedes hacer uso de bibliotecas existenes como nltk (kit de
herramientas de lenguaje natural), newspaper3k y gtts (puedes seguir las instrucciones de
instalación de pip).
Puedes crear un programa al que proporcionarle una URL de un artículo a convertir para
luego manejar la conversión de texto a voz.
'''
#primero importamos las librerias que nos interesan
from gtts import gTTS #para pasar de texto a audio
from newspaper import Article #para pasarle un url y extraer los strings de ellos
import os #para ejecutar audio en el codigo y eliminarlo.

#definimos las funciones
def pedir_comprobar_url():
    '''En esta funcion pediremos al usuario un url y verificaremos que existe, y si es asi lo delvolveremos'''
    
    url = input('Introduce un url de una pagina web en español para leerlo(Para pegar el url debes presionar Ctrl + Mayus + V): ')   
    articulo = Article(url, language = 'es')
    try:
        articulo.download()
        articulo.parse()
        articulo.nlp()
    except:
        print('Url no valida')
    else:
        return articulo

def texto_a_audio(articulo):
    '''En esta funcion recibiremos el articulo descargado y extraeremos el texto y el titulo y lo convertiremos a audio'''
    titulo_articulo = articulo.title
    texto_articulo =articulo.text.replace('\n','')
    texto = titulo_articulo +'\n'+ texto_articulo
    texto_a_sonido =gTTS(texto, lang ='es')
    return texto_a_sonido

def guardar_leer(sonido):
    '''En esta funcion borraremos si existe un audio antes y luego lo guardaremos el sonido y lo leeremos'''
    try:
        os.remove('audio.mp3')
    except FileNotFoundError:
        pass
    sonido.save('audio.mp3')
    os.system('audio.mp3')


#implementamos el codigo del programa
articulo = pedir_comprobar_url()       
if articulo:#si articulo tiene valor es decir url es correcta pues seguimos sino el programa acaba
    #pasamos de texto a audio el articulo
    sonido = texto_a_audio(articulo)
    #lo guardamos y lo leemos
    guardar_leer(sonido)


    