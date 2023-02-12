# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.
# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

user_number = int(input('Enter a number: '))
my_list = list(range(user_number))
print(my_list)
second_list = []
j = 0
from random import randrange
while j < user_number:
    for i in range(user_number):
            ran = randrange(user_number)
            if ran not in second_list:
                second_list.append(ran)
                j = j+1
print(second_list)

# ---------------------------------------------------------------
# Вариант из проверки дз, 

from random import randrange

num = int(input('Enter a number: '))
nums_list = list(range(num))
res_list = []

print(nums_list)

for i in range(num):
    n_1, n_2 = randrange(num), randrange(num)
    nums_list[n_1], nums_list[n_2] = nums_list[n_2], nums_list[n_1] # Используем метод кортежей (позиция, значение)

print(nums_list)

# --------------------------------------------
nums_list = list(range(22,33))
print(nums_list)
for i, val in enumerate(nums_list):
    print(i, val)



    