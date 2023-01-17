import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

star, = plt.plot([], [], '-', color='r', label='Star')

alpha = np.arange(0, 0.4 * np.pi, 0.1)
x = 12 * np.cos(alpha) + 8 * np.cos(1.5 * alpha)
y = 12 * np.sin(alpha) - 8 * np.sin(1.5 * alpha)

def rotate(t):
    t = t * np.pi / 180
    X = x * np.cos(alpha) - y * np.sin(alpha)
    Y = y * np.cos(alpha) + x * np.sin(alpha)
    return X, Y

def animate(i):
    star.set_data(rotate(t=i))
    return x, y

edge = 25
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ani = FuncAnimation(fig, animate, frames = 200, interval = 30)

ani.save('lec_7_complexobject.gif')
