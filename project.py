import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

fig = plt.figure()
ax = plt.axes(xlim=(0, 5), ylim=(-1.5, 1.5))
line, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    return line,

def animate(i):
    x = np.linspace(0, 5, 500)
    y = np.sin(2 * np.pi * (x + 0.02 * i))
    line.set_data(x, y)
    return line,

ani = FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

ani.save('project.gif')
