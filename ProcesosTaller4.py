import numpy as np
import pygame as pg


colorBlanco = np.array([255, 255, 255])
colorGris1 = np.array([225, 225, 225])
colorGris2 = np.array([200, 200, 200])
colorGris3 = np.array([175, 175, 175])
colorGris4 = np.array([150, 150, 150])
colorGris5 = np.array([125, 125, 125])
colorGris6 = np.array([100, 100, 100])
colorGris7 = np.array([75, 75, 75])
colorGris8 = np.array([50, 50, 50])
colorGris9 = np.array([25, 25, 25])
colorNegro = np.array([0, 0, 0])
colorAmarillo = np.array([255, 255, 0])
colorAzul = np.array([0, 0, 255])
colorRojo = np.array([255, 0, 0])
colorVerde = np.array([0, 255, 0])
colorNaranja = np.array([255, 127, 0])
colorMorado = np.array([163, 73, 164])
colorCian = np.array([0, 225, 225])
colorMagenta = np.array([255, 20, 147])
colorGris = np.array([150, 152, 154])
colorMarron = np.array([141, 73, 37])



'''
Nombre : BarraHerramientas1()
Objetivo : mostrar en una ventana una matriz de colores
Parametros : miVentana --> ventana donde se mostraran los colores
retorna : la matriz de colores
'''

def BarraHerramientas1(miVentana):
    #Area de colores
    pg.draw.rect(miVentana, colorCian, [0, 0, 80, 80])
    pg.draw.rect(miVentana, colorBlanco, [80, 0, 80, 80])
    pg.draw.rect(miVentana, colorRojo, [160, 0, 80, 80])

    pg.draw.rect(miVentana, colorMagenta, [0, 80, 80, 80])
    pg.draw.rect(miVentana, colorGris, [80, 80, 80, 80])
    pg.draw.rect(miVentana, colorVerde, [160, 80, 80, 80])

    pg.draw.rect(miVentana, colorAmarillo, [0, 160, 80, 80])
    pg.draw.rect(miVentana, colorNegro, [80, 160, 80, 80])
    pg.draw.rect(miVentana, colorAzul, [160, 160, 80, 80])

'''
Nombre : BarraHerramientas2()
Objetivo : mostrar en una ventana una imagen de colores a raiz de una matriz
Parametros : miVentana2 --> ventana donde se mostraran los colores
retorna :  la imagen de colores
'''

def BarraHerramientas2(miVentana2):
    #Area de colores
    pg.draw.rect(miVentana2, colorAmarillo, [0, 0, 40, 300])
    pg.draw.rect(miVentana2, colorCian, [40, 0, 80, 300])
    pg.draw.rect(miVentana2, colorVerde, [120, 0, 80, 300])
    pg.draw.rect(miVentana2, colorMagenta, [200, 0, 80, 300])
    pg.draw.rect(miVentana2, colorRojo, [280, 0, 80, 300])
    pg.draw.rect(miVentana2, colorAzul, [360, 0, 80, 300])
    pg.draw.rect(miVentana2, colorBlanco, [0, 300, 40, 80])
    pg.draw.rect(miVentana2, colorGris1, [40, 300, 40, 80])
    pg.draw.rect(miVentana2, colorGris2, [80, 300, 40, 80])
    pg.draw.rect(miVentana2, colorGris3, [120, 300, 40, 80])
    pg.draw.rect(miVentana2, colorGris4, [160, 300, 40, 80])
    pg.draw.rect(miVentana2, colorGris5, [200, 300, 40, 80])
    pg.draw.rect(miVentana2, colorGris6, [240, 300, 40, 80])
    pg.draw.rect(miVentana2, colorGris7, [280, 300, 40, 80])
    pg.draw.rect(miVentana2, colorGris8, [320, 300, 40, 80])
    pg.draw.rect(miVentana2, colorGris9, [360, 300, 40, 80])
    pg.draw.rect(miVentana2, colorNegro, [400, 300, 40, 80])

'''
Nombre : InversoImagen(Imagen)
Objetivo : invertir los colores de una imagen 
Parametros : Imagen --> imagen en formato jpg se recomienda dividir la imagen en 255
retorna : la imagen con los colores invertidos
'''
def InversoImagen(Imagen):
    Imagen1=np.copy(Imagen)
    Imagen1=1-Imagen
    return(Imagen1)

'''
Nombre : CapaRoja(Imagen)
Objetivo : Recibe una imagen y retorna la capa roja
Parametros : Imagen --> imagen en formato jpg se recomienda dividir la imagen en 255
retorna : la imagen con capa roja
'''
def CapaRoja(Imagen):
    CapaRed=np.copy(Imagen)
    CapaRed[:,:,1]=0
    CapaRed[:,:,2]=0
    return(CapaRed)

'''
Nombre : CapaVerde(Imagen)
Objetivo : Recibe una imagen y retorna la capa verde
Parametros : Imagen --> imagen en formato jpg se recomienda dividir la imagen en 255
retorna : la imagen con capa verde
'''
def CapaVerde(Imagen):
    CapaGreen=np.copy(Imagen)
    CapaGreen[:,:,0]=0
    CapaGreen[:,:,2]=0
    return(CapaGreen)
'''
Nombre : CapaAzul(Imagen)
Objetivo : Recibe una imagen y retorna la capa azul
Parametros : Imagen --> imagen en formato jpg se recomienda dividir la imagen en 255
retorna : la imagen con capa azul
'''
def CapaAzul(Imagen):
    CapaBlue=np.copy(Imagen)
    CapaBlue[:,:,0]=0
    CapaBlue[:,:,1]=0
    return(CapaBlue)
'''
Nombre : CapaMagenta(Imagen)
Objetivo : Recibe una imagen y retorna la capa magenta
Parametros : Imagen --> imagen en formato jpg se recomienda dividir la imagen en 255
retorna : la imagen con capa magenta
'''
def CapaMagenta(Imagen):
    CapaM=np.copy(Imagen)
    CapaM[:,:,2]=1
    CapaM[:,:,0]=1
    return(CapaM)
'''
Nombre : CapaCyan(Imagen)
Objetivo : Recibe una imagen y retorna la capa cyan
Parametros : Imagen --> imagen en formato jpg se recomienda dividir la imagen en 255
retorna : la imagen con capa cyan
'''
def CapaCyan(Imagen):
    CapaC=np.copy(Imagen)
    CapaC[:,:,1]=1
    CapaC[:,:,2]=1
    return(CapaC)
'''
Nombre : CapaAmarilla(Imagen)
Objetivo : Recibe una imagen y retorna la capa amarilla
Parametros : Imagen --> imagen en formato jpg se recomienda dividir la imagen en 255
retorna : la imagen con capa amarilla
'''
def CapaAmarilla(Imagen):
    CapaY=np.copy(Imagen)
    CapaY[:,:,0]=1
    CapaY[:,:,1]=1
    return(CapaY)
'''
Nombre : SumaCapas(R,G,B)
Objetivo : reconstruir los colores de una imagen a raiz de sus capas
Parametros : R --> capa roja
             G --> capa verde
             B --> capa azul
retorna : la imagen compuesta por las capas RGB
'''
def SumaCapas(R,G,B):
    CapasSum=np.copy(R+G+B)
    return(CapasSum)
'''
Nombre : SumaImagenes(Imagen1,Imagen2)
Objetivo : Recibe 2 imagenes y las suma 
Parametros : Imagen1 --> imagen en formato jpg se recomienda dividir la imagen en 255
             Imagen2 --> imagen en formato jpg se recomienda dividir la imagen en 255
retorna : la suma de las 2 imagenes
'''
def SumaImagenes(Imagen1,Imagen2):
    Suma=Imagen1+Imagen2
    return(Suma)
'''
Nombre : SumaImagenesEcu(Imagen1,Imagen2,Factor)
Objetivo : Recibe 2 imagenes , las suma y las ecualiza  
Parametros : Imagen1 --> imagen en formato jpg se recomienda dividir la imagen en 255
             Imagen2 --> imagen en formato jpg se recomienda dividir la imagen en 255
             Factor --> es el facotr de acualizacion
retorna : la suma de las 2 imagenes ecualizadas
'''
def SumaImagenesEcu(Imagen1,Imagen2,Factor):
    Suma=(Imagen1 * Factor) + ((Factor-1) * Imagen2)
    return(Suma)
'''
Nombre : EcualImagen(Imagen,Factor)
Objetivo : Recibe una imagen y deacuerdo a un factor la ecualiza 
Parametros : Imagen --> imagen en formato jpg se recomienda dividir la imagen en 255
             Factor --> este es el factor de ecualizacion             
retorna : la imagen ecualizada
'''
def EcualImagen(Imagen,Factor):
    NewIm=np.copy(Imagen)
    NewIm=NewIm*Factor
    return(NewIm)
'''
Nombre : GrisAverage(Imagen)
Objetivo : Recibe una imagen y la retorna en grises con la tectica de average 
Parametros : Imagen --> imagen en formato jpg se recomienda dividir la imagen en 255
retorna : la imagen en grises con la tecnica de promedio de average
'''
def GrisAverage(Imagen):
    Filas, Columnas, Capas = np.shape(Imagen)
    Img2=np.copy(Imagen)
    for i in range(Filas):
        for j in range(Columnas):
            Img2[i,j]= np.average(Imagen[i,j])
    return(Img2)
'''
Nombre : GrisLuminosity(Imagen)
Objetivo : Recibe una imagen y la retorna en grises con la tectica de luminosity
Parametros : Imagen --> imagen en formato jpg se recomienda dividir la imagen en 255
retorna : la imagen en grises con la tecnica de luminosity
'''
def GrisLuminosity(Imagen):
    Filas, Columnas, Capas = np.shape(Imagen)
    Img=np.copy(Imagen)
    for i in range(Filas):
        for j in range(Columnas):
            Img[i,j]= Imagen[i,j,0]*0.299+Imagen[i,j,1]*0.587+Imagen[i,j,2]*0.114
    return(Img)
'''
Nombre : GrisMidgray(Imagen)
Objetivo : Recibe una imagen y la retorna en grises con la tectica de midgray
Parametros : Imagen --> imagen en formato jpg se recomienda dividir la imagen en 255
retorna : la imagen en grises con la tecnica de midgray
'''
def GrisMidgray(Imagen):
    Filas, Columnas, Capas = np.shape(Imagen)
    Img=np.copy(Imagen)
    for i in range(Filas):
        for j in range(Columnas):
            Img[i,j]= (max(Imagen[i,j,0],Imagen[i,j,1],Imagen[i,j,2])+
            min(Imagen[i,j,0],Imagen[i,j,1],Imagen[i,j,2]))/2
    return(Img)