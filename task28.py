# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
#
# *Пример:*
# 2 2
#     4

A = int(input("Введите число А: "))
B = int(input("Введите число B: "))


def sum(a, b):
    if b < 1:
        return a
    return a + sum(1, b - 1)


print(sum(A, B))
