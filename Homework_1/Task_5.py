# 5. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# https://ru.onlinemschool.com/math/library/analytic_geometry/point_point_length/
# in
# - 3
# - 6
# - 2
# - 1

x1 = int(input('Enter x1:'))
y1 = int(input('Enter y1:'))
x2 = int(input('Enter x2:'))
y2 = int(input('Enter y2:'))


def f(a1, b1, a2, b2):
    doublex = (a1-a2)*(a1-a2)
    doubley = (b1-b2)*(b1-b2)
    import math
    sqrt = math.sqrt(doublex+doubley)
    return round(sqrt)

print(f(x1, y1, x2, y2))
