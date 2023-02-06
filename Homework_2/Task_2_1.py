# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# Без работы с методами строк.
# in -> out
# - 6782 -> 23
# - 0.67 -> 13
# - 198.45 -> 27

number = str(input('Enter a number: '))
no_dots = int(number.replace(".", ""))
sum = int(0)
while no_dots > 0:
    sum = sum + no_dots % 10
    no_dots = no_dots//10

print(sum)
