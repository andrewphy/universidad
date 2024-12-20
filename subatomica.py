# -*- coding: utf-8 -*-
"""subatomica.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1FKnLpfjSXIXIjCSkE5O1dGP6pcHCzOtX
"""

import numpy as np
 import matplotlib.pyplot as plt
 import math
 from scipy.misc import derivative

def V(r,l):
  V=(-2)/r +l*(l+1)/r**2
  return V
r=np.arange(0.5,10,0.1)
plt.plot(r,V(r,1))
plt.plot(r,V(r,2))
plt.plot(r,V(r,4))
plt.ylabel(r"$V_{eff}(r)$ [Ryd]")
plt.title(r"$V_{eff}^{l}(r)$ vs r")
plt.grid(True)
plt.xlabel(r"r [Ryd]")
plt.legend([r"$V_{eff}^{1}(r)$",r"$V_{eff}^{2}(r)$",r"$V_{eff}^{4}(r)$"])
plt.ylim(-1,1)
plt.axhline(y=0, color='black', linestyle='--')
plt.savefig("Potencial_efectivo.png")
plt.show()

from scipy.special import assoc_laguerre #Polinomios asociados de Laguerre
def U(n,l,r):
  U=((2/n)**3*(math.factorial(n-l-1)/(2*n*math.factorial(n+l))))**(1/2)*np.exp(-r/n)*(2/n)**l *np.power(r,l+1)*assoc_laguerre(2*r/n,n-l-1,2*l+1)
  return U
r=np.arange(0.5,15,0.1)
plt.plot(r,U(1,0,r))
plt.plot(r,U(2,0,r))
plt.plot(r,U(2,1,r))
plt.axhline(y=0, color='black', linestyle='--')
plt.xlabel(r"r [a_0]")
plt.ylabel(r"$U_{nl}(r)$")
plt.title(r"$U_{nl}(r)$ vs r")
plt.legend([r"$U_{1,s}(r)$",r"$U_{2,s}(r)$",r"$U_{2,p}(r)$"])
plt.grid(True)
plt.savefig("Funcion_radial_atomoH.png")
plt.show()

import numpy as np
import matplotlib.pyplot as plt
beta_values = [1, 2]  # Valores de beta
k_values = [1, 2]     # Valores de k
theta = np.linspace(0, np.pi, 500)  # Ángulo de dispersión

# Función para calcular f(theta)
def scattering_amplitude(k, beta, theta):
    q = 2 * k * np.sin(theta / 2)
    f_theta = 4*beta*np.sqrt(np.pi)*(np.exp(-1*np.divide((q*beta)**2,4))-96*np.exp(-1*((q*beta)**2)))
    return f_theta

# Calcular y graficar dσ/dΩ
plt.figure(figsize=(8, 6))
for k in k_values:
  for b in beta_values:
    f_theta = scattering_amplitude(k, b, theta)
    dsigma_domega = np.abs(f_theta)**2  # dσ/dΩ
    plt.plot(np.degrees(theta), dsigma_domega, label=f"k={k}, β={b}")

# Personalización de la gráfica
plt.xlabel(r"$\theta$ (grados)", fontsize=14)
plt.xlim(0,30)
plt.ylabel(r"$\frac{d\sigma}{d\Omega}$", fontsize=14)
plt.title("Distribución angular elástica", fontsize=16)
plt.legend(fontsize=12)
plt.grid()
plt.savefig('punto5.jpg')
plt.show()

from os import access
# prompt: hallar la parabola de masa para 5 isotopos isobaricos

import numpy as np
import matplotlib.pyplot as plt

# Datos de los isóbaros
A = 128  # Número de masa

Z_values = [60,58,56,54,52,50,48]  # Números atómicos de los isóbaros
masses = [-60.53,-75.534,-85.369,-89.86,-88.993,-83.361,-67.238 ] #Excess mass
x=np.linspace(Z_values[-1],Z_values[0],100)
#cst modelo gota liquida
av,ass,ac,asy,ap=15.83,18.33,0.714,23.2,11.2
mn=939.6
mp=938.3
#parabola Teorica
def M(A,Z):
  p1=mn-av+np.divide(ass,np.power(A,(1/3)))+asy
  p2=(mp-mn)-ac/np.power(A,(1/3))-4*asy
  p3=(ac)*(np.power(A,-1/3))+4*(asy/A)
  parry=np.divide(ap*(-1**Z),np.power(A,(1/2)))
  print(p2,p3)
  return (p1*A)+(p2*Z)+(p3*np.power(Z,2))-A*931.5-parry

#Parabola experimental
y=np.polyfit(Z_values, masses, 2)
x=np.linspace(Z_values[-1],Z_values[0],100)
# Graficar la parábola de masas
plt.figure(figsize=(8, 6))
plt.plot(Z_values, masses, 'o', markersize=8,label='Datos')
plt.plot(x, np.polyval(y, x), 'c--', linewidth=2,label=r"Ajuste $y = {:.1f}x^2  {:.1f}x + {:.0f}$".format(y[0], y[1], y[2]))
plt.plot(x,M(A,x),label='Curva Teorica')
#Flechas
plt.arrow(Z_values[-1], masses[-1],1.8, masses[-2] - masses[-1]+1,head_width=0.2, head_length=0.5, fc='r', ec='r')
plt.arrow(Z_values[-2], masses[-2],1.5, masses[-3] - masses[-2]+1,head_width=0.2, head_length=0.5, fc='r', ec='r')
plt.arrow(Z_values[4], masses[4],1.2, masses[3] - masses[4]-1,head_width=0.2, head_length=0.5, fc='r', ec='r')
plt.arrow(Z_values[0], masses[0], -1.8, masses[1] - masses[0],     head_width=0.2, head_length=0.5, fc='r', ec='r')
plt.arrow(Z_values[1], masses[1], -1.6, masses[2] - masses[1]+2,     head_width=0.2, head_length=0.5, fc='r', ec='r')
plt.arrow(Z_values[2], masses[2], -1.5, masses[3] - masses[2]+1.6,     head_width=0.2, head_length=0.5, fc='r', ec='r')
plt.text(49,-75,r'$\beta -$')
plt.text(50,-87,r'$\beta -$')
plt.text(53,-93,r'$\beta -$')
plt.text(59,-72,r'$\beta +$')
plt.text(57,-87,r'$\beta +$')
plt.text(55,-93,r'$\beta +$')
# Personalizar la gráfica
plt.xlabel("Número atómico (Z)", fontsize=14)
plt.ylabel("Diferencia de masa [Mev]", fontsize=14)
plt.title(f"Parábola de masas para A = {A}, par-par", fontsize=16)
plt.legend()
plt.grid(True)
plt.savefig('punto7.png')
plt.show()

Ai = 115  # Número de masa

Zi_values = [55,53,51,49,47,45,43]  # Números atómicos de los isóbaros
imasses = [-59.7,-76.338,-87.003,-89.536,-84.983,-74.229,-55.8] #Excess mass
x=np.linspace(Zi_values[-1],Zi_values[0],100)
#Parabola experimental
yi=np.polyfit(Zi_values, imasses, 2)
xi=np.linspace(Zi_values[-1],Zi_values[0],100)
# Graficar la parábola de masas
plt.figure(figsize=(8, 6))
plt.plot(Zi_values, imasses, 'o', markersize=8,label='Datos')
plt.plot(xi, np.polyval(yi, xi), 'c--', linewidth=2,label=r"Ajuste $y = {:.1f}x^2  {:.1f}x + {:.0f}$".format(yi[0], yi[1], yi[2]))
plt.plot(xi,M(Ai,xi),label='Curva Teorica')
#Flechas
plt.arrow(Zi_values[-1],imasses[-1],1.8,  imasses[-2] - imasses[-1],head_width=0.2, head_length=0.5, fc='r', ec='r')
plt.arrow(Zi_values[-2],imasses[-2],1.5,  imasses[-3] - imasses[-2]+1,head_width=0.2, head_length=0.5, fc='r', ec='r')
plt.arrow(Zi_values[4], imasses[4],1.4,   imasses[3] -  imasses[4],head_width=0.2, head_length=0.5, fc='r', ec='r')
plt.arrow(Zi_values[0], imasses[0], -1.8, imasses[1] -  imasses[0],     head_width=0.2, head_length=0.5, fc='r', ec='r')
plt.arrow(Zi_values[1], imasses[1], -1.7, imasses[2] -  imasses[1]+3,     head_width=0.2, head_length=0.5, fc='r', ec='r')
plt.arrow(Zi_values[2], imasses[2], -1.5, imasses[3] -  imasses[2]+1,     head_width=0.2, head_length=0.5, fc='r', ec='r')
plt.text(44,-75,r'$\beta -$')
plt.text(45.7,-87,r'$\beta -$')
plt.text(47.7,-93,r'$\beta -$')
plt.text(50,-86,r'$\beta +$')
plt.text(52,-79,r'$\beta +$')
plt.text(54,-71,r'$\beta +$')
# Personalizar la gráfica
plt.xlabel("Número atómico (Z)", fontsize=14)
plt.ylabel("Diferencia de masa [Mev]", fontsize=14)
plt.title(f"Parábola de masas para A = {Ai}, impar-impar", fontsize=16)
plt.legend()
plt.grid(True)
plt.savefig('punto7i.png')
plt.show()

import numpy as np
import matplotlib.pyplot as plt

# Valores de j (momento angular total)
j_values = np.arange(0.5, 5, 0.5)

# Constantes de Landé para protones y neutrones
g_s_proton = 5.585  # Proton spin gyromagnetic factor
g_l_proton = 1      # Proton orbital gyromagnetic factor
g_s_neutron = -3.826  # Neutron spin gyromagnetic factor
g_l_neutron = 0       # Neutron orbital gyromagnetic factor

# Líneas de Schmidt para protones
mu_proton_j_up = g_l_proton * (j_values - 0.5) + 0.5 * g_s_proton
mu_proton_j_down = (j_values / (j_values + 1)) * (g_l_proton * (j_values + 0.5) - 0.5 * g_s_proton)

# Líneas de Schmidt para neutrones
mu_neutron_j_up = g_l_neutron * (j_values - 0.5) + 0.5 * g_s_neutron
mu_neutron_j_down = (j_values / (j_values + 1)) * (g_l_neutron * (j_values + 0.5) - 0.5 * g_s_neutron)

# Graficar
plt.figure(figsize=(10, 6))

# Proton
jp= [1/2,3/2,3/2,3/2,3/2,5/2,7/2,7/2,5/2,3/2,1/2,7/2,1/2,3/2,7/2,5/2,5/2,3/2,1/2,7/2,5/2,]
up=[2.79284734462,-0.2814,0.1468,2.1107,3,2.7,4.526,5.34,0.69,2.56,0.159,4.34,0.71,1.38,4.47,3.49,3.3,-0.386,0.49,2.318,0.8456]
jn=[1/2,5/2,3/2,3/2,5/2,5/2,3/2,5/2,5/2,3/2,9/2,5/2,9/2,7/2,5/2,1/2,1/2,7/2,1/2,5/2,9/2]
un=[-1.9130427,-0.531,0.2032,0.1633,0.701,-0.68,0.75,-0.7382,-0.84,0.39,-0.894,-1.3,-1.09,-0.94,0.68,-0.099,-0.937,1.37,-1,-1.89,-0.794]
plt.plot(j_values, mu_proton_j_up, 'k--', label=r'Proton $j = l + 1/2$')
plt.plot(j_values, mu_proton_j_down, 'k--', label=r'Proton $j = l - 1/2$')
plt.plot(jp,up,'ro')
# Configuración de la gráfica
plt.text(2,4.5,r'$j=l+\frac{1}{2}$',rotation=20,fontsize=12)
plt.text(2.5,-0.2,r'$j=l-\frac{1}{2}$',rotation=15,fontsize=12)
plt.title('Líneas de Schmidt para Protones', fontsize=16)
plt.xlabel('Momento Angular Total $j$', fontsize=14)
plt.ylabel('Momento Magnético $\\mu$ ($\\mu_N$)', fontsize=14)
plt.savefig('protones.png')
#plt.grid(alpha=0.4)
plt.tight_layout()


# Neutron
plt.figure(figsize=(10, 6))
plt.plot(j_values, mu_neutron_j_up, 'k--', label=r'Neutron $j = l + 1/2$')
plt.plot(j_values, mu_neutron_j_down, 'k--', label=r'Neutron $j = l - 1/2$')
plt.plot(jn,un,'ro')
# Configuración de la gráfica
plt.text(2,-1.8,r'$j=l+\frac{1}{2}$',color='k',fontsize=12)
plt.text(2,1.3,r'$j=l-\frac{1}{2}$',color='k',rotation=10,fontsize=12)
plt.title('Líneas de Schmidt para Neutrones', fontsize=16)
plt.xlabel('Momento Angular Total $j$', fontsize=14)
plt.ylabel('Momento Magnético $\\mu$ ($\\mu_N$)', fontsize=14)
#plt.grid(alpha=0.4)
plt.tight_layout()

# Mostrar

plt.savefig('neutrones.png')
plt.show()

def I(E,j):
  h=6.582*(10**(-19))
  return np.divide(h**2,E)*j*(j+1)
j=[2,4,6,8,10,12]
E=[105.9,342.7,694.1,1141.50,1665.35,2244.45]

print(I(np.array(E),np.array(j)))