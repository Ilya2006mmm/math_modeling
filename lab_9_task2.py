import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 40, 1)

def radio_function(m, t):
    dmdt = -k * m * t
    return dmdt

m_0 = 1000
k = 8/100

m_t = odeint(radio_function, m_0, t)

plt.plot(t, m_t[:,0], label = 'Инвестиции')
plt.xlabel('Инвестиционное время, месяцы')
plt.ylabel('Инвестиционная функция')
plt.title('Инвестиции')
plt.legend()

plt.savefig('aab.png')