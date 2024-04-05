import numpy as np
import matplotlib.pyplot as plt
'''
Nombre : Brillo(Imagen,Factor)
Objetivo : Cambiar el brillo de una imagen 
Parametros : Imagen --> imagen en formato jpg se recomienda dividir la imagen en 255
             Facor --> factor de ajuste de brillo de la imagen 
retorna : la imagen con el brillo ajustado 
'''
def Brillo(Imagen,Factor):
    return(Imagen+Factor)


'''
Nombre : BrilloCanal(Imagen,Canal,Factor)
Objetivo : Cambiar el brillo de una imagen segun el canal
Parametros : Imagen --> imagen en formato jpg se recomienda dividir la imagen en 255
             Canal --> un valor numerico entre 0 y 2 que indica la capa que se va mostrar
             Facor --> factor de ajuste de brillo de la imagen 
retorna : la imagen con el brillo ajustado 
'''

def BrilloCanal(Imagen,Canal,Factor):
    Imagen[:,:,Canal]= Imagen[:,:,Canal]+Factor
    return(Imagen)
'''
Nombre : Contraste(Imagen,Tipo,Factor)
Objetivo : Cambiar el Contraste de una imagen variando la ecuacion con la que lo hace
Parametros : Imagen --> imagen en formato jpg se recomienda dividir la imagen en 255
             Tipo -->  1 o 2 es el tipo de ecuacion que se utilia
             Facor --> factor de ajuste del contraste de la imagen 
retorna : la imagen con el contraste ajustado 
'''


def Contraste(Imagen,Tipo,Factor):
    if Tipo==1:
        Imagen = Factor*np.exp(Imagen-1)
    else:
        Imagen = Factor*np.log10(1+Imagen)
    return(Imagen)

    
'''
Nombre : Zoom(Imagen,alpha,pinicial)
Objetivo : Cambiar el Contraste de una imagen variando la ecuacion con la que lo hace
Parametros : Imagen --> imagen en formato jpg se recomienda dividir la imagen en 255
             Tipo -->  1 o 2 es el tipo de ecuacion que se utilia
             Facor --> factor de ajuste del contraste de la imagen 
retorna : la imagen con el contraste ajustado 
'''


def MiZoom(Imagen,alpha,PuntoI,PuntoJ):
    
    filas,columnas,col=np.shape(Imagen)
    beta=alpha
    zoom=np.copy(Imagen)
    for i in range(filas) :
        for j in range(columnas) :
            zoom[i,j]=Imagen[round(alpha*i+PuntoI),round(beta*j+PuntoJ)]
    
    return(zoom)
