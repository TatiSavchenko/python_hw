# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.

# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод –
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом,
# собирает ягоды с этого куста и с двух соседних с ним.

# Напишите программу для нахождения максимального числа ягод,
# которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random

bush = int(input("Введите количество кустов черники на грядке: "))

berries = [random.randint(50, 100) for i in range(bush)]
print(berries)

bush_count = []
for i in range(len(berries) - 1):
    bush_count.append(berries[i - 1] + berries[i] + berries[i + 1])
bush_count.append(berries[-2] + berries[-1] + berries[0])
bush_count.append(berries[0] + berries[1] + berries[2])

print(max(bush_count))


