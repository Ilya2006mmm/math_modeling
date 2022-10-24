a = 1
b = 1
c = int(input())
print(a)
print(b)
d = a + b
while d <= c:
    print(d)
    b, d = d, b + d