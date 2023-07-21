# Задача №19
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# import random
from random import randint as rd  # alias(псевдоним)


n = int(input("Введите кол-во элементов списка: "))
data_list = list()
for i in range(n):
    data_list.append(rd(-5, 5))
print(data_list)

k = int(input("Введите кол-во сдвигов: "))
result_list = []
k = k % n
for i in range(k):
    result_list.append(data_list[n - k + i])
for i in range(n - k):
    result_list.append(data_list[i])
print(result_list)
