# 3. Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.Без использования
# встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000

# in
# 11
# out
# 1011

number = int(input('Enter a decimal number: '))
list = []
while number > 0:
    list.append(number % 2)
    number = number//2


def reverse_list(f_list):
    length = len(f_list)
    i = 0
    k = 0
    while i <= (length-1)//2:
        k = f_list[i]
        f_list[i] = f_list[length-1-i]
        f_list[length-1-i] = k
        i = i+1
    print(f_list)

reverse_list(list)

# ----------------------------------------------------------
# ----------------------------------------------------------
# Вариант из проверки дз

def conv_bin(num: int):
    list_nums = []

    while num > 0:
        list_nums.insert(0, num % 2)
        num //= 2

    print(*list_nums, sep="") # Распечатает список без скобочек, но при этом это останется список


conv_bin(int(input()))
