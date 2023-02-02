# 3. Напишите программу, которая принимает на вход координаты
# точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер
# четверти плоскости, в которой находится эта точка
# (или на какой оси она находится).
# *Пример:*

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x = int(input('Enter X: '))
y = int(input('Enter y: '))
print(x, y)
if x > 0 and y > 0:
    print(f'The dot {x,y} is in the 1 quarter')
elif x < 0 and y > 0:
    print(f'The dot {x,y} is in the 2 quarter')
elif x < 0 and y < 0:
    print(f'The dot {x,y} is in the 3 quarter')
elif x>0 and y<0:
    print(f'The dot {x,y} is in the 4 quarter')
else:
    print(f"The dot {x,y} doesn't belong to any quarter")
