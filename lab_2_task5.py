a = int(input())
b = int(input())
c = a / b
d = a % b
if (a > 0 or a < 0) and b != 0:
  print('Делится')
  print("Частное:", c)
elif b == 0:
  print('Делитель не должен равняться 0')
else:
    print('Не делится')
    print('Остаток:', a % b)






