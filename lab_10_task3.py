import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

y = np.arange(-1, 1, 0.01)

	
def diff_func(sys, y):
    z, y = sys 
    dy_dt = z
    dz_dy = np.sin(y) + np.cos(y)
    return dy_dt, dz_dy


y0 = 3
dy0_dt = 0
sys0 = y0, dy0_dt

sol = odeint(diff_func, sys0, y)


plt.plot(y, sol[:, 1], 'b', label='theta(t)')

plt.legend()
plt.savefig('pic5.png')