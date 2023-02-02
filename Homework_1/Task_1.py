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