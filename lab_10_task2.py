import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(-1, 1, 0.01)

	
def diff_func(sys, x):
    y, t = sys 
    dx_dt = 3 * x - 2 * y + ((np.e ** (3 * t)) / np.e ** t + 1)
    dy_dt = x - ((np.e ** (3 * t)) / np.e ** t + 1)
    return dx_dt, dy_dt


y0 = -7
x0 = 5
sys0 = y0, x0

sol = odeint(diff_func, sys0, x)


plt.plot(x, sol[:, 1], 'b', label='theta(t)')

plt.legend()
plt.savefig('pic4.png')