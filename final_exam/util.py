import numpy as np
from numpy import random
import matplotlib.pyplot as plt

#
# para Problema 1
#
def inicializar_fekete(n,semilla=42):
    """
    Devuelve n puntos al azar sobre la esfera
    """
    rng = random.default_rng(semilla)
    X = rng.normal(size=(3,n))
    return X /np.outer(np.ones(3),np.linalg.norm(X,axis=0))
    
    
def mostrar_fekete(X):
    """
    muestra los puntos en 3D
    """
    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(projection='3d')
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.scatter(X[0,:],X[1,:],X[2,:],marker='o',s=9)
    plt.show()



#
# Para problema 2
#
def generar_A(m=1000,p=100,semilla=42):
    rng = random.default_rng(semilla)
    A = rng.normal(size=(m,p))
    A -= np.outer(np.ones(m),np.mean(A,axis=0))
    A /= np.outer(np.ones(m),np.linalg.norm(A,axis=0))
    return A


def generar_y(semilla=42):
    rng = random.default_rng(semilla)
    y = rng.normal(size=(1000))
    y = y - np.mean(y)
    return y


