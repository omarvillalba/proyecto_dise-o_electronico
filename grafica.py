#importación de modulos
import math 
import numpy as np
from matplotlib import pyplot as plt

#generaciion de arreglos
x = np.array(range(200))*0.1
y = np.zeros(len(x))
for i in range(len(x)):
    y[i] = math.sin(x[i])

#creacion de graficos
plt.title("Funcion seno") 

plt.xlabel("eje X")
plt.ylabel("eje y")

plt.plot(x, y)
plt.show()

