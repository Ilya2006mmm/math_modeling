import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

x = np.arange(0, 10, 0.01)

	
def diff_func(z, x):
    y, omega = z 
    dy_dx = omega 
    domega_d = np.sin(y) * z - 3 * x * y - 5
    return dy_dx, domega_d


y0 = 0.01
omega0 = 0.05


z0 = y0

sol = odeint(diff_func, z0, x)


plt.plot(x, sol[:, 1], 'b', label='y(x)')

plt.legend()
plt.savefig('pic2.png')