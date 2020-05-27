#importación de modulos
import math 
import numpy as np

#generaciion de arreglos
x = np.array(range(20))*0.1
y = np.array(len(x))
for i in range(len(x)):
    y[i] = math.sin(x[i])

#creacion de graficos
