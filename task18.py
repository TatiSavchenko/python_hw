# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X
#
# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5

import random

list = [random.randint(0, 50) for i in range(20)]
print(list)

find_number = int(input("Введите число, которое хотите найти в списке: "))

list.sort()
print(list)

left_nearest = None
right_nearest = None
i = 0

while find_number in list:
    print("Число найдено в списке")
    break
else:
    while i < len(sorted(list)):
        if list[i] < find_number:
            left_nearest = list[i]

        else:
            if list[i] > find_number:
                right_nearest = list[i]
                break
        i += 1

    print(left_nearest)
    print(right_nearest)

    diff1 = find_number - left_nearest
    diff2 = find_number - right_nearest

if diff1 == diff2:
    print(f'Равноценно близкие по величине: {left_nearest}, {right_nearest}')

elif diff1 > diff2:
    print(f'Число в списке не найдено, но ближайшее к нему по величине = {left_nearest}')
else:
    print(f'Число в списке не найдено, но ближайшее к нему по величине = {right_nearest}')


