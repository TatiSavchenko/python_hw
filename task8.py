# Задача 8: Требуется определить,
# можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

length_of_chocolate = int(input("Введите длину шоколадки: "))
width_of_chocolate = int(input("Введите ширину шоколадки: "))
size = length_of_chocolate*width_of_chocolate
pieces_of_chocolate = int(input("Введите количество долек: "))
if pieces_of_chocolate<size:
    if pieces_of_chocolate%length_of_chocolate==0 or pieces_of_chocolate%width_of_chocolate==0:
        print("YES")
    else:
        print("NO")