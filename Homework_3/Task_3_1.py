# 1. Задайте список, состоящий из произвольных чисел, количество задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

# in
# 4
# out
# [4, 2, 4, 9]
# 8

from random import sample

user_number = int(input('Enter the number of elements: '))


def form_list(number, in_range=100):
    in_list = []
    for i in range(number):
        in_list = sample(range(in_range), k=number) # Можно проще, смотри ниже
        return in_list


def find_sum(list):
    in_sum = 0
    for i in range(len(list)):
        if i % 2 == 0:
            in_sum += list[i]
    return in_sum
      

my_list = form_list(user_number)
print(my_list)
my_sum = find_sum(my_list)
print(my_sum)

# # -----------------------------------------------------------
# # -------------------------------------------------------------

# # вариант из проверки дз
# from random import sample

# #  проверка чисел на положительность и формирование списка
# def list_rand_nums(count: int) -> list: #  в скобках указан тип данных, после стрелки тип возвращаемых данных
#     if count < 0:
#         print("Negative value of the number of numbers!")
#         return []

#     list_nums = sample(range(1, count * 2), count) # CСоздаем список (откуда, сколько)
#     return list_nums


# def sum_odd_pos(list_nums: list):
#     sum_nums = 0
#     for k in range(0, len(list_nums), 2):
#         sum_nums += list_nums[k]
#     return sum_nums


# all_list = list_rand_nums(int(input("Number of numbers: ")))
# print(all_list)
# print(sum_odd_pos(all_list))