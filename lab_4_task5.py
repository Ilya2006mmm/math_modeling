
def figures(circle, rectangle, triangle):
    circle = input()
    if input() == circle:
        print('Круг')
        print('Ведите радиус круга (число пи вводится автоматом)')
        r = int(input())
        pi = 3.14
        s_circle = pi * r ** 2
        print(s_circle)
    rectangle = input()
    if input() == rectangle:
        print('Прямоугольник')
        print('Ведите длины сторон прямоугольника')
        a = int(input())
        b = int(input())
        s_rectangle = a * b
        print(s_rectangle)
    triangle = input()
    if input() == triangle:
        print('Треугольник')
        print('Ведите длину стороны треугольника')
        g = int(input())
        print('Ведите длину высоты треугольника')
        h = int(input())
        s_triangle = (g * h) / 2
        print(s_triangle)
        

print(figures())



