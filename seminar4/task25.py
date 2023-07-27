# Задача №25
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

text = input("Введите текст: ").split()
count_char = {}
for char in text:
    if char not in count_char:
        print(char, end=" ")
        count_char[char] = 1
    else:
        print(f'{char}_{count_char[char]}', end=' ')
        count_char[char] += 1
        