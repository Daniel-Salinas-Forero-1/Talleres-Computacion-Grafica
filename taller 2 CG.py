import numpy as np
import os 
def Punto1():
    M=np.array([[0,2,4,6],[0,3,5,7]])
    np.savetxt('matriz.txt',M,fmt = '%d' )
    b=np.loadtxt('matriz.txt')
    print(b)
    print("segunda fila",M[1])
    print("cuarta columna", M[:,3])
    print("submatriz del ejercicio",M[0:,:2])
#Punto1()
def Punto2():
    A=np.array([[1,3,5,8],[2,6,5,3],[4,1,9,7],[1,8,0,2]])
    B=np.array([[1,9,5,8],[12,5,5,9],[4,2,9,74],[0,6,0,3]])
    C=np.array([[1,9],[10,2]])
    print('Matriz A = \n',A)
    print('Matriz B = \n',B)
    print('Matriz C = \n',C)
    print('3 * A = \n',3*A)
    print('A - 7= \n',A-7)
    print('A * B**T = \n',B.T*A)
    print('A**-1 = \n',np.linalg.inv(A))
    print('B**-1 = \n',np.linalg.inv(B))
#Punto2()