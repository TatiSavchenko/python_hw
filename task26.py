# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8

number_A = int(input("Введите число А: "))
number_B = int(input("Введите число B:"))


def degree_number(a, b):
    result = 0
    if b == 1:
        return a
    return (a * degree_number(a,b-1))

print(degree_number(number_A,number_B))


        
        
