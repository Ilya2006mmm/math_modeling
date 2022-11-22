def my_func(a = 1, b = 0):
    x = 3 * a - b
    return x

print(my_func())
print(my_func(3, 4))
print(my_func(b = 3))
print(my_func(b = 3, a = 9))

def my_funct(a, b = 0):
    x = 3 * a - b
    return x


def my_functi(*args):
    x = 3 * args[0] - args[1]

print(my_functi(3, 4))
print(my_functi(3, 4, 8))

def my_functio(**kw):
    x = 3 * kw['obj_1'] - kw['obg_2']

print(my_functio(obj_1 = 3, obj_2 = 4))
