# 1. Напишите программу, которая принимает на вход цифру, обозначающую 
# день недели, и проверяет, является ли этот день выходным.
# *Пример:*

# - 6 -> да
# - 7 -> да
# - 1 -> нет


a = int(input("Enter a number: "))
if 1 <= a < 6:
    print("workday")
elif a==6 or a==7:
    print("weekend")
else:
    print("There is no such day of the week. Enter other number.")

# Можно решить через range

a = int(input("Enter a number: "))
if a in range(1,6):
    print("workday")
elif a in range(6,8):
    print("weekend")
else:
    print("There is no such day of the week. Enter other number.")

# По умолчанию в range начальное значение 0 и шаг 1 (range(0,21,1)), 
# поэтому их можно не писать(range(21)).