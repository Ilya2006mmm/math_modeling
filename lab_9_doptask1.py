import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

R = 6400000
h = 50 * R
r = np.arange(h + R, R, -1000)

def f(v, r):
    dvdr = - G * M / (v * r ** 2)
    return dvdr

G = 6.67 * 10 ** (-11)
M = 6 * 10 ** 24
v0 = 1
    
vr = odeint(f, v0, r)

plt.plot(vr[:,0], label = 'Распад')
plt.title()
plt.legend()

plt.savefig('aс.png')
