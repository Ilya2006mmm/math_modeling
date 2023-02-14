import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
 
teta = np.arange(0, 2*np.pi, 0.01)
 
def energy(w, teta):
    dwdteta = 1 / 4 * R_earth**2 * L_sun / (q * v_q)
    return dwdteta


w_0 = 0
R_earth = 6400000
L_sun = 3.827 * 10**(26)
q = 147 * 10**9
v_q = 30400

solve = odeint(energy, w_0, teta)

plt.plot(teta*180/np.pi, solve[:,0])
plt.xlabel('Оборот, градусы')
plt.ylabel('Солнечная энергия, Дж')
plt.title('Освещенность Земли')
plt.grid()

plt.savefig('pic1.jpg')