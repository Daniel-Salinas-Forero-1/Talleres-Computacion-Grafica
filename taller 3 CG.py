import numpy as np
import matplotlib.pyplot as plt
import math



def Factorial(n):
    if(n ==0 or n==1):
        r=1
    elif(n>1):
        r=n*Factorial(n-1)
    else:
        return("NaN")
    return(r)



def MiSeno(x):
    AporteMin=0.000001
    Sum=0
    Termino=0
    n=0
    while(True):
        Termino= ((-1)**n)/(Factorial(2*n+1))*x**(2*n+1)
        n=n+1
        Sum=Sum+Termino
        if(math.fabs(Termino)<AporteMin):
            break
    return(Sum)




def GraficaSeno():
    plt.figure("Ejemplo función seno")
    plt.title("Función seno")
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")
    x=np.linspace(0,2*math.pi,100)
    i=0
    while(i<100):
        y=MiSeno(x[i])
        plt.plot(x[i],y,'.')
        i=i+1
    plt.show()


#MiSeno(0.5)
#GraficaSeno()


def MiCoseno(x):
    AporteMin=0.0001
    Sum=0
    Termino=0
    n=0
    while(True):
        Termino= ((-1)**n)/(Factorial(2*n))*x**(2*n)
        n=n+1
        Sum=Sum+Termino
        if(math.fabs(Termino)<AporteMin):
            break
    return(Sum)



def GraficaCoseno():
    plt.figure("Ejemplo función seno")
    plt.title("Función Coseno")
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")
    x=np.linspace(0,2*math.pi,100)
    i=0
    while(i<100):
        y=MiCoseno(x[i])
        plt.plot(x[i],y,'.')
        i=i+1
    plt.show()


#MiCoseno(0.5)
#GraficaCoseno()

def Euler(x):
    AporteMin=0.0001
    Sum=0
    Termino=0
    n=0
    while(True):
        Termino= ((x)**n)/(Factorial(n))
        n=n+1
        Sum=Sum+Termino
        if(math.fabs(Termino)<AporteMin):
            break
    return(Sum)



def GraficaEuler():
    plt.figure("Ejemplo función seno")
    plt.title("Función Euler")
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")
    x=np.linspace(0,2*math.pi,100)
    i=0
    while(i<100):
        y=Euler(x[i])
        plt.plot(x[i],y,'.')
        i=i+1
    plt.show()


#Euler(1)
#GraficaEuler()


def Logaritmo(x):
    Aportemin=0.000001
    Aportemax=10000
    Sum=0
    n=1
    while (True):
        termino=(((-1)**(n+1))/n)*x**n
        Sum+=termino
        if math.fabs(termino)< Aportemin or math.fabs(termino)> Aportemax:
            break
        n+=1
    return Sum
    


def GraficaLogaritmo():
    plt.figure("Ejemplo función seno")
    plt.title("Función Euler")
    plt.xlabel("Eje x")
    plt.ylabel("Eje y")
    x=np.linspace(0,1,100)
    for i in range(0,100):
        y=Logaritmo(x[i])
        plt.plot(x[i],y,'.')
    plt.show()


#Logaritmo(2)
#GraficaLogaritmo()
