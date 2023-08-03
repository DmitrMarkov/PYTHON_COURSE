# Задача №43
# Дан список чисел. Посчитайте, сколько в нем пар
# элементов, равных друг другу. Считается, что любые
# два элемента, равные друг другу образуют одну пару,
# которую необходимо посчитать. Вводится список
# чисел. Все числа списка находятся на разных
# строках.
# Ввод:         Вывод:
# 1 2 3 2 3     2

from random import randint as rd

count1 = int(input("Введите кол-во элементов массива: "))
list1 = [rd(1,5) for _ in range(count1)]
print(list1)
pairs = 0
for item in set(list1):
    print(item, list1.count(item))
    pairs += list1.count(item) // 2
print(pairs)
# print(sum([list1.count(item) // 2 for item in set(list1)]))
# Вывод в одну строку
