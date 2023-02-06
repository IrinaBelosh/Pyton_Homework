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
    



# for i in range(user_number): #0
#     while i < user_number:
#         if randrange(user_number) not in second_list:
#             second_list.append(randrange(user_number+1))
# print(second_list)
