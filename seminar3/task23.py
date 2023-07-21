# Задача №23
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 
# Пояснение: (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

from random import randint as rd


n = int(input("Введите кол-во элементов: "))
data_list = list()
for i in range(n):
    data_list.append(rd(-10, 10))
print(data_list)
count = 0
for i in range(n - 1):
    if data_list[i + 1] > data_list[i]:
        count += 1
        print(f'{data_list[i + 1]} > {data_list[i]}')
print(count)  
