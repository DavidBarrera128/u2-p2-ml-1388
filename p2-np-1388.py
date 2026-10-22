import numpy as np
# David Barrera NC = 1388
# Ejemplos de numpy numerical python
print("-- Espaciado Linealmente en array -- 1388")
arre=np.linspace(start=0,stop=5,num=5)
print(arre)
print("-- matriz identidad en 20 array -- 1388")
matrix = np.eye(3)
print(matrix)
print("-- Generar numeros al azar (Aleatorios) en 2D array -- 1388")
numale = np.random.random((3,4))
print(numale)
print("generar 9 numeros aleatorios entre 0 y 1")
numale = np.random.random((3,3))# Genera 12 numeros aleatorios
print(numale)
# como generar 9 numeros aleatorios comprendidos entre 1 y 20
# con numpy en un arreglo de 3 por 3
print("generar 9 numeros aleatorios entre 1 y 20")
arre = np.random.randint(1, 21, size=9).reshape(3,3)
print(arre)
print("David Barrera NC = 1388")