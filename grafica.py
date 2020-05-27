#importación de modulos
import math 
import numpy as np
from matplotlib import pyplot as plt

#generaciion de arreglos
x = np.array(range(200))*0.1
y = np.zeros(len(x))
for i in range(len(x)):
    y[i] = math.sinh(x[i])

# Generamos un segundo conjunto de datos para el gráfico
x_2 = np.array(range(200))*0.1
y_2 = np.zeros(len(x_2))
for j in range(len(x_2)):
    y_2[j] = math.cos(x_2[j])

#creacion de graficos

plt.subplot(211)
plt.xlabel("eje X")
plt.ylabel("eje y") 
plt.legend(['Seno hiperbolico'])
plt.title("Funcion seno hiperbolico") 
plt.plot(x,y)

plt.subplot(212)
plt.xlabel("eje X")
plt.ylabel("eje y") 
plt.legend(['Coseno'])
plt.title("Funcion coseno") 
plt.plot(x_2,y_2)


plt.show()

