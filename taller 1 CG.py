import numpy as np
#1
#Cree el siguiente vector  A= [2, 3,5, 1, 4 ,7 9, 8, 6, 10] 
A = np.array([2,3,5,1,4,7,9,8,6,10])
#print(A)


#2
#Cree un vector B que contenga los elementos desde el 11 hasta el 20 (utilice subscripts)
B = np.arange(11,21)
#print(B)


#3
#Componer un vector C formado por los vectores A y B en la misma fila respectivamente
C = np.append(A,B,axis=0)
#print(C)


#4
#encuentre el valor mínimo en el vector C haciendo uso de la función propia de Numpy 
#print(np.min(C))


#5
#encuentre el valor máximo en el vector C haciendo uso de la  función propia de Numpy
#print(np.max(C))


#6
#encuentre la longitud en el vector C haciendo uso de la  función propia de Numpy
#print(len(C))


#7
#encuentre la suma de los elementos el vector C haciendo uso de la función propia de Numpy 
#print(np.sum(C))


#8
#encentre el promedio de los elementos en el vector C haciendo uso de las operaciones elementales suma y división 
#print(np.sum(C)/len(C))


#9
#Encuentre el promedio en el vector C haciendo uso de la función propia de Numpy
#print(np.mean(C))


#10
#Encuentre la media en el vector C haciendo uso de la función propia de Numpy 
#print(np.median(C))


#12
# Cree un vector D a partir del vector C con los elementos mayores que 5 
D=np.array([])

for i in C:
    if i>5:
        D = np.append(D,i)

#print(D)


#13
#Cree un vector E a partir del vector C con los elementos mayores que 5 y menores que 15
E=np.array([])

for i in C:
    if i>5:
        if i<15:
            E = np.append(E,i)

#print(E)


#14
#Cambie los elementos 5 y 15 elemento del vector C por ‘7’ 
np.putmask(C,C==5,7)
np.putmask(C,C==15,7)
#print(C)


#15
#determine la moda del vector C 
y=0
z=0
for i in C:
    x=0
    for j in C: 
        if i==j:
            x+=1    
    if x > y:   
        z=i
        y=x
#print("la moda del vector C es : ",z)


#16
#ordene el Vector C de menor a mayor
C=np.sort(C)
#print(C)


#17
#Multiplique el vector C por 10 
C=C*10
#print(C)


#18
#Cambie los elementos del 6 al 8 de la matriz C por 60, 70 y 80 respectivamente 
C[6]=60
C[7]=70
C[8]=80
#print(C)


#19
C[14]=140
C[15]=150
C[16]=160
#print(C)








































































