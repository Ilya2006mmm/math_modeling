import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 10**3, 1)

def radio_function(m, t):
    dmdt = k * m
    return dmdt

m_0 = 1
k = 1/10 ** 2

m_t = odeint(radio_function, m_0, t)

plt.plot(t, m_t[:,0], label = 'Распад')
plt.xlabel('Период распада, минуты')
plt.ylabel('Функция распада')
plt.title('Радиоактивный распад')
plt.legend()

plt.savefig('aaa.png')