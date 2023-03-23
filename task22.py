# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа.
# n - кол-во элементов первого множества. m - кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

import random

num_N = int(input("Введите кол-во элементов первого множества set1: "))
num_M = int(input("Введите кол-во элементов второго множества set2: "))

list1 = [random.randint(0, num_N) for i in range(num_N+1)]
list2 = [random.randint(0, num_M) for i in range(num_M+1)]

print(list1)
print(list2)

set1 = set(list1)   #множества не содержат дубликатов элементов
set2 = set(list2)

#print(set1)
#print(set2)

set_output = set1.union(set2)   # x.union(y, z) объединение двух множеств
print(set_output)