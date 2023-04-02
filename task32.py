# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

my_list = [random.randint(0,100) for i in range(20)]
print(my_list)

min = int(input("Введите мин значение диапазона: "))
max = int(input("Введите макс значение диапазона: "))

for i in range(len(my_list)):
    if min <= my_list[i] <= max:
        print(i, end=' ,')


