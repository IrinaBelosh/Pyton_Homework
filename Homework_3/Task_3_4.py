# * 4. Задайте список из произвольных вещественных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов. (Сравнивать надо не числа, а сразу дробные части!)
# in
# 5
# out
# [5.16, 8.62, 6.57, 7.92, 9.22]
# Min: 0.16, Max: 0.92. Difference: 0.76

# in
# 3
# out
# [9.26, 8.5, 1.14]
# Min: 0.14, Max: 0.5. Difference: 0.36

from random import uniform
import math

user_number = int(input('Enter the number of elements: '))


def form_list(number):
    in_list = []
    for i in range(number):
        variable = round(uniform(1, 10), 2)
        in_list.append(variable)
    return in_list


def find_minmax(in_list, num_elem): # Не сразу поняла задание
    a = 0
    b = 0
    if in_list[0] < in_list[1]:
        min = in_list[0]
        max = in_list[1]
        for i in range(num_elem):
            if i >= 2:
                if in_list[i] < min:
                    min = in_list[i]
                elif in_list[i] > max:
                    max = in_list[i]
            a = math.floor(min)
            b = math.floor(max)
        return (round((min - a),2), round((max - b), 2))



my_list = form_list(user_number)
print(my_list)
find_minmax(my_list, user_number)
a,b = find_minmax(my_list, user_number)
print(round((b-a),2))

# ----------------------------------------------
# ----------------------------------------------
# Вариант из проверки дз
from random import uniform


def list_rand_nums(count: int):
    list_nums = []
    if count <= 0:
        print("Negative value of the number of numbers!")
        return [0.0]

    for i in range(count):
        list_nums.append(round(uniform(1, count), 2))
    return list_nums


def dif_max_min(list_nums: list):
    num_max = num_min = list_nums[0] % 1 # Сразу оставляем дробную часть

    for k in range(1, len(list_nums)):
        num = round(list_nums[k] % 1, 2) # Сразу оставляем дробную часть
        if num > num_max:
            num_max = num
        elif num < num_min:
            num_min = num

    result = round(num_max - num_min, 2) # В функции сразу записываем(!) разницу с округлением
    print(f"Min: {num_min}, Max: {num_max}. Difference: {result}")
    return result


all_list = list_rand_nums(int(input("Number of numbers: ")))
print(all_list)
print(dif_max_min(all_list))










