import pygame as pg
import numpy as np
import matplotlib.pyplot as plt
from pyparsing import punc8bit
import ProcesosTaller4 as proc4


def Punto1():
    colorNegro = np.array([0, 0, 0])
    if __name__ == "__main__":
        miVentana = pg.display.set_mode((240, 240))
        miVentana.fill(colorNegro)
        runnig = True
    
        while (runnig):
            proc4.BarraHerramientas1(miVentana)
            pg.display.update()
            for eventos in pg.event.get():
            
                if (eventos.type == pg.QUIT):
                    runnig = False
                    exit()

#Punto1()


def Punto2():
    colorNegro = np.array([0, 0, 0])
    if __name__ == "__main__":
        miVentana2 = pg.display.set_mode((440, 380))
        miVentana2.fill(colorNegro)
        runnig = True
    
        while (runnig):
            proc4.BarraHerramientas2(miVentana2)
            pg.display.update()
            for eventos in pg.event.get():
            
                if (eventos.type == pg.QUIT):
                    runnig = False
                    exit()    

#Punto2()

def Punto3():
    MiImagen=plt.imread("foto.JPG")
    plt.figure("Daniel Foto")
    plt.subplot(1,2,1)
    plt.title("imagen 1")
    plt.imshow(MiImagen)
  
    MiImagen2=proc4.InversoImagen((MiImagen)/255)
    plt.subplot(1,2,2)
    plt.title("imagen 2")
    plt.imshow(MiImagen2)
    plt.show()

#Punto3()

def Punto4():
    MiImagen=plt.imread("foto.JPG")
    plt.figure("Daniel Foto")
    plt.subplot(1,2,1)
    plt.title("imagen 1")
    plt.imshow(MiImagen)
  
    MiImagen2=proc4.CapaRoja((MiImagen)/255)
    plt.subplot(1,2,2)
    plt.title("imagen 2")
    plt.imshow(MiImagen2)
    plt.show()

#Punto4()

def Punto5():
    MiImagen=plt.imread("foto.JPG")
    plt.figure("Daniel Foto")
    plt.subplot(1,2,1)
    plt.title("imagen 1")
    plt.imshow(MiImagen)
  
    MiImagen2=proc4.CapaVerde((MiImagen)/255)
    plt.subplot(1,2,2)
    plt.title("imagen 2")
    plt.imshow(MiImagen2)
    plt.show()

#Punto5()

def Punto6():
    MiImagen=plt.imread("foto.JPG")
    plt.figure("Daniel Foto")
    plt.subplot(1,2,1)
    plt.title("imagen 1")
    plt.imshow(MiImagen)
  
    MiImagen2=proc4.CapaAzul((MiImagen)/255)
    plt.subplot(1,2,2)
    plt.title("imagen 2")
    plt.imshow(MiImagen2)
    plt.show()

#Punto6()


def Punto7():
    MiImagen=plt.imread("foto.JPG")
    plt.figure("Daniel Foto")
    plt.subplot(1,2,1)
    plt.title("imagen 1")
    plt.imshow(MiImagen)
  
    MiImagen2=proc4.CapaMagenta((MiImagen)/255)
    plt.subplot(1,2,2)
    plt.title("imagen 2")
    plt.imshow(MiImagen2)
    plt.show()

#Punto7()


def Punto8():
    MiImagen=plt.imread("foto.JPG")
    plt.figure("Daniel Foto")
    plt.subplot(1,2,1)
    plt.title("imagen 1")
    plt.imshow(MiImagen)
  
    MiImagen2=proc4.CapaCyan((MiImagen)/255)
    plt.subplot(1,2,2)
    plt.title("imagen 2")
    plt.imshow(MiImagen2)
    plt.show()

#Punto8()


def Punto9():
    MiImagen=plt.imread("foto.JPG")
    plt.figure("Daniel Foto")
    plt.subplot(1,2,1)
    plt.title("imagen 1")
    plt.imshow(MiImagen)
  
    MiImagen2=proc4.CapaAmarilla((MiImagen)/255)
    plt.subplot(1,2,2)
    plt.title("imagen 2")
    plt.imshow(MiImagen2)
    plt.show()

#Punto9()

def Punto10():
    MiImagen=plt.imread("foto.JPG")
    MiImagenR=proc4.CapaRoja((MiImagen)/255)
    plt.figure("Foto Daniel")
    plt.subplot(2,2,1)
    plt.title("Capa R")
    plt.imshow(MiImagenR)
  


    MiImagenV=proc4.CapaVerde((MiImagen)/255)
    plt.subplot(2,2,2)
    plt.title("Capa V")
    plt.imshow(MiImagenV)

    MiImagenA=proc4.CapaAzul((MiImagen)/255)
    plt.subplot(2,2,3)
    plt.title("Capa A")
    plt.imshow(MiImagenA)

    MiImagen2 = proc4.SumaCapas(MiImagenR,MiImagenV,MiImagenA) 
    plt.subplot(2,2,4)
    plt.title("suma de las capas")
    plt.imshow(MiImagen2)
    plt.show()

#Punto10()


def Punto11():
    MiImagen=plt.imread("foto2.JPG")
    plt.figure("Daniel Foto")
    plt.subplot(2,2,1)
    plt.title("imagen 1")
    plt.imshow(MiImagen)


    MiImagen2=plt.imread("foto3.JPG")
    plt.subplot(2,2,2)
    plt.title("imagen 2")
    plt.imshow(MiImagen2)


    ImagenSum = proc4.SumaImagenes(MiImagen,MiImagen2)
    plt.subplot(2,2,3)
    plt.title("imagen 3")
    plt.imshow(ImagenSum)
    plt.show()
    

#Punto11()


def Punto12():
    MiImagen=plt.imread("foto2.JPG")
    plt.figure("Daniel Foto")
    plt.subplot(2,2,1)
    plt.title("imagen 1")
    plt.imshow(MiImagen)


    MiImagen2=plt.imread("foto3.JPG")
    plt.subplot(2,2,2)
    plt.title("imagen 2")
    plt.imshow(MiImagen2)

    
    ImagenSumEcu = proc4.SumaImagenesEcu(MiImagen/255,MiImagen2/255,0.6)
    plt.subplot(2,2,3)
    plt.title("imagen 3")
    plt.imshow(ImagenSumEcu)
    plt.show()
    

#Punto12()


def Punto13():
    MiImagen=plt.imread("foto2.JPG")
    plt.figure("Daniel Foto")
    plt.subplot(1,2,1)
    plt.title("imagen 1")
    plt.imshow(MiImagen)
    
    ImagenEcu = proc4.EcualImagen(MiImagen/255,5)
    plt.subplot(1,2,2)
    plt.title("imagen 2")
    plt.imshow(ImagenEcu)
    plt.show()
    

#Punto13()


def Punto14():
    MiImagen=plt.imread("foto.JPG")
    plt.figure("Daniel Foto")
    plt.subplot(1,2,1)
    plt.title("imagen 1")
    plt.imshow(MiImagen)
    
    Imagen = proc4.GrisAverage(MiImagen)
    plt.subplot(1,2,2)
    plt.title("imagen 2")
    plt.imshow(Imagen)
    plt.show()
    

#Punto14()

def Punto15():
    MiImagen=plt.imread("foto.JPG")
    plt.figure("Daniel Foto")
    plt.subplot(1,2,1)
    plt.title("imagen 1")
    plt.imshow(MiImagen)
    
    Imagen = proc4.GrisAverage(MiImagen)
    plt.subplot(1,2,2)
    plt.title("imagen 2")
    plt.imshow(Imagen)
    plt.show()
    
#Punto15()




def Punto16():
    MiImagen=plt.imread("foto.JPG")
    plt.figure("Daniel Foto")
    plt.subplot(1,2,1)
    plt.title("imagen 1")
    plt.imshow(MiImagen)
    
    Imagen = proc4.GrisLuminosity(MiImagen)
    plt.subplot(1,2,2)
    plt.title("imagen 2")
    plt.imshow(Imagen)
    plt.show()
    

#Punto16()

def Punto17():
    MiImagen=plt.imread("foto.JPG")
    plt.figure("Daniel Foto")
    plt.subplot(1,2,1)
    plt.title("imagen 1")
    plt.imshow(MiImagen)
    
    Imagen = proc4.GrisMidgray(MiImagen)
    plt.subplot(1,2,2)
    plt.title("imagen 2")
    plt.imshow(Imagen)
    plt.show()
    

#Punto17()