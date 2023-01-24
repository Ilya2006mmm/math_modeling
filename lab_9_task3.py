import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 30, 1)

g = 10

y = 0.3


def radio_function(m, y, v, g = 10, t):
    dmdt = g - y/m * v ** 2
    return dmdt


m_t = odeint(radio_function, m, t)

plt.plot(t, m_t[:,0], label = 'Распад')
plt.xlabel('Период распада, минуты')
plt.ylabel('Функция распада')
plt.title('Радиоактивный распад')
plt.legend()

plt.savefig('aaс.png')