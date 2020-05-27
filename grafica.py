#importación de modulos
import math 
import numpy as np
from matplotlib import pyplot as plt

#generaciion de arreglos
x = np.array(range(200))*0.1
y = np.zeros(len(x))
for i in range(len(x)):
    y[i] = math.sin(x[i])

# Generamos un segundo conjunto de datos para el gráfico
x_2 = np.array(range(200))*0.1
y_2 = np.zeros(len(x_2))
for j in range(len(x_2)):
    y_2[j] = math.cos(x_2[j])

#creacion de graficos
plt.title("Funcion seno y coseno") 

plt.xlabel("eje X")
plt.ylabel("eje y") 
plt.legend(['Seno','Coseno'])


plt.plot(x,y,'bo',x_2,y_2,'y-')

plt.show()

