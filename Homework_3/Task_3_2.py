# 2. Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д. (в C# стр 47)
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]

# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import sample

user_number = int(input('Enter the number of elements: '))


def form_list(number, in_range=10): # Можн покороче, смотри в примере ниже
    in_list = []
    for i in range(number):
        in_list = sample(range(in_range), k=number)
        return in_list


def find_mult(f_list):
    second_list = []
    length = len(f_list)
    # print(length, second_list)
    i = 0
    mult = 0
    while i <= (length-2)//2: # Во втором варианте код короче
        mult = (f_list[i]) * (f_list[(length-1)-i])
        second_list.append(mult)
        i = i+1
    if length % 2 != 0:
        second_list.append(f_list[length//2])
    return second_list


my_list = form_list(user_number)
print(my_list)
mult = find_mult(my_list)
print(mult)

# --------------------------------------------------------
# --------------------------------------------------------
# Вариант из проверки дз

from random import sample


def list_rand_nums(count): # Формируем список
    if count < 0:
        print("Negative value of the number of numbers!")
        return []

    list_nums = sample(range(1, count * 2), count)
    return list_nums


def prod_pairs(list_nums: list):
    res_list = []
    len_list = len(list_nums)

    for k in range(len_list // 2):
        res_list.append(list_nums[k] * list_nums[len_list - k - 1])

    if len_list % 2:
        res_list.append(list_nums[len_list // 2])
    return res_list


all_list = list_rand_nums(int(input("Number of numbers: ")))
print(all_list)
print(prod_pairs(all_list))
