import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

y = np.arange(-5, 5, 0.01)

	
def diff_func(sys, y):
    z, y = sys 
    dy_dt = z
    dz_dy = -4 * z + 5 * y
    return dy_dt, dz_dy


y0 = 4
dy0_dt = -1
sys0 = y0, dy0_dt

sol = odeint(diff_func, sys0, y)


plt.plot(y, sol[:, 1], 'b', label='theta(t)')

plt.legend()
plt.savefig('pic6.png')