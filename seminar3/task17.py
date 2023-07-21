# Задача №17
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# import random
from random import randint as rd  # alias(псевдоним)


n = int(input("Введите кол-во элементов списка: "))
data_list = list()
for i in range(n):
    data_list.append(rd(-5, 5))
print(data_list)
print(len(set(data_list)))
