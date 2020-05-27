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
    # Generamos un tercero conjunto de datos para el gráfico
x_3 = np.array(range(200))*0.1
y_3 = np.zeros(len(x_3))
for j in range(len(x_3)):
    y_3[j] = math.exp(x_3[j])
    # Generamos un cuarto conjunto de datos para el gráfico
x_4 = np.array(range(200))*0.1
y_4 = np.zeros(len(x_4))
for j in range(len(x_4)):
    y_4[j] = math.sqrt(x_4[j])

#creacion de graficos


plt.subplot(221)
plt.xlabel("eje X")
plt.ylabel("eje y") 
plt.legend(['Seno'])
plt.title("Funcion seno") 
plt.plot(x,y)

plt.subplot(222)
plt.xlabel("eje X")
plt.ylabel("eje y") 
plt.legend(['Coseno'])
plt.title("Funcion coseno") 
plt.plot(x_2,y_2)

plt.subplot(223)
plt.xlabel("eje X")
plt.ylabel("eje y") 
plt.legend(['Exponencial'])
plt.title("Funcion expoencial") 
plt.plot(x_3,y_3)

plt.subplot(224)
plt.xlabel("eje X")
plt.ylabel("eje y") 
plt.legend(['sqrt'])
plt.title("Funcion raiz cuadrada") 
plt.plot(x_4,y_4)

plt.show()