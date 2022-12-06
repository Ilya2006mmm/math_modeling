import matplotlib.pyplot as plt
import numpy as np

def square(a = 1, b = 1, c = 0, title = 's'):
    x = np.arange(-10, 10, 0.01)
    y = a * b
    plt.plot(x, y, label = 's')
    plt.xlabel('Coord: x')
    plt.ylabel('Coord: y')
    plt.legend()
    plt.title(title)
    plt.grid()

square()
plt.savefig('pic_1.png')





    









