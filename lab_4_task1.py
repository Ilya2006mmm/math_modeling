import numpy as np
def summ(a):
    s = 0
    for i in range(len(a)):
        s = s + a[i]
    print(s / len(a))
    
a = [7, 8, 6, 5, 19]
summ(a)

