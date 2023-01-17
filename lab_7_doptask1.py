import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

ball, = plt.plot([], [], 'o', color='r', label='Ball')
cyc, = plt.plot([], [], 'o', color='b', label='Ball')
trajectory, =  plt.plot([], [], 'o', color='b', label='Ball')

def cycloida(R, time):
    x = R * (time - np.sin(time)) - R
    y = R * (1 - np.cos(time))  - R
    return x, y


def circle_move(R, vx0, vy0, time):
    x0 = vx0 * time
    y0 = vy0 * time
    alpha = np.arange(0, 2 * np.pi, 0.1)
    x = x0 + R * np.cos(alpha) - R
    y = y0 + R * np.sin(alpha)
    return x, y

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

x, y = [], []

def animate(i):
    ball.set_data(circle_move(R = 0.5, vx0 = 0.01, vy0 = 0, time = i))
    coords = cycloida(R=0.5, time=i/50)
    x.append(coords[0])
    y.append(coords[1])
    cyc.set_data(x[i], y[i])
    trajectory.set_data(x, y)


ani = FuncAnimation(fig, animate, frames = 200, interval = 30)

ani.save('lab_7_doptask1.gif')
