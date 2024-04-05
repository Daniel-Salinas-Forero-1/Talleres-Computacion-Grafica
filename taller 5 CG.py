#1
import numpy as np
import matplotlib.pyplot as plt
import ProcesosTaller5 as proc5
def punto1():

    MiImagen=plt.imread("foto.JPG")
    plt.figure("Daniel Foto")
    plt.subplot(1,2,1)
    plt.title("imagen 1")
    plt.imshow(MiImagen)
  
    factor = float(input("ingrese el factor de brillo de la imagen valores de entre -1 hasta 1 : "))
    MiImagen2=proc5.Brillo((MiImagen)/255,factor)
    plt.subplot(1,2,2)
    plt.title("imagen 2")
    plt.imshow(MiImagen2)
    plt.show()

punto1()

def punto2():
    MiImagen=plt.imread("foto.JPG")
    plt.figure("Daniel Foto")
    plt.subplot(1,2,1)
    plt.title("Mi imagen original")
    plt.imshow(MiImagen)

    factor = float(input("ingrese el factor de brillo de la imagen valores de entre -1 hasta 1 : "))
    canal = int(input("ingrese el canal a modificar 0,1,2 : "))
    MiImagen2=proc5.BrilloCanal((MiImagen)/255,canal,factor)
    plt.subplot(1,2,2)
    plt.title("imagen 2")
    plt.imshow(MiImagen2)

    plt.show()
#punto2()

def punto3():
    MiImagen=plt.imread("foto.JPG")
    plt.figure("Daniel Foto")
    plt.subplot(1,2,1)
    plt.title("Mi imagen original")
    plt.imshow(MiImagen)

    factor = float(input("ingrese el factor de brillo de la imagen valores de entre 0 hasta 10 : "))
    tipo = int(input("ingrese el Tipo de contraste tipo 1 o tipo 2 : "))
    MiImagen2=proc5.Contraste((MiImagen)/255,tipo,factor)
    plt.subplot(1,2,2)
    plt.title("imagen 2")
    plt.imshow(MiImagen2)

    plt.show()
#punto3()


def punto4():
    MiImagen=plt.imread("foto.JPG")
    plt.figure("Daniel Foto")
    plt.subplot(1,2,1)
    plt.title("Mi imagen original")
    plt.imshow(MiImagen)

    porcentaje = float(input("ingrese el porcentaje de zoom se da entre 0 y 0.7 por efectos de la imagen : "))
    puntox = int(input("ingrese el punto en el eje X donde se va hacer zoom : "))
    puntoy = int(input("ingrese el punto en el eje Y donde se va hacer zoom : "))
    MiImagen2=proc5.MiZoom(MiImagen/255,porcentaje,puntox,puntoy)
    plt.subplot(1,2,2)
    plt.title("imagen 2")
    plt.imshow(MiImagen2)

    plt.show()
#punto4()






























