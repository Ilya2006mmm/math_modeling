import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ball, = plt.plot([], [], '-', color='r', label='Ball')

def circle_move(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0, 2 * np.pi, 0.1)
    x = x0 + R * np.cos(alpha) ** 3
    y = y0 + R * np.sin(alpha) ** 3
    return x, y

edge = 1
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    ball.set_data(circle_move(R = 0.05, vx0 = 0.005, vy0 = 0.005, time = i))

ani = FuncAnimation(fig, animate, frames = 180, interval = 30)

ani.save('lec_7_complexobject.gif')
