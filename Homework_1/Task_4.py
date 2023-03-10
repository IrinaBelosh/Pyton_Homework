# 4. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).
# *Пример:*

# - 1 -> x > 0, y > 0
# - 8 -> нет такой четверти

# quarter = int(input('Enter the number of a quarter: '))
# if quarter == 1:
#     print('x > 0 and y > 0')
# elif quarter == 2:
#     print('x < 0 and y > 0')
# elif quarter == 3:
#     print('x < 0 and y < 0')
# elif quarter == 4:
#     print('x > 0 and y < 0')
# else:
#     print('There is not such quarter. Enter other number')

# Решение через match
quarter = input('Enter the number of a quarter: ')
match quarter:
    case "1":
        print('x > 0 and y > 0')
    case "2":
        print('x < 0 and y > 0')
    case "3":
        print('x < 0 and y < 0')
    case "4":
        print('x > 0 and y < 0')
    case _:
        print('There is not such quarter. Enter other number')
