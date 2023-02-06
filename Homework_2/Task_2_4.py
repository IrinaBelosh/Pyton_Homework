# * 4. Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните 
# числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20

# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

k = int(input('Enter a number: '))
position_1 = int(input('Enter the position of the first digit: '))
position_2 = int(input('Enter the position of the second digit: '))
mult = 0
list = list(range(-k, k+1))
print(list)

if position_1 and position_2 <= k*2:
    mult = list[position_1-1] * list[position_2-1]
    print(mult)
elif position_1 == 0 or position_2 == 0:
    print('The enumeration starts with 1!')
else:
    print('There is no value for these indexes!')
