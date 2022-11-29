import numpy as np

def y(a, b, N):
    x = np.linspace(a, b, N)
    y = x ** 2
    print(y)

y(-10, 10, 100)


