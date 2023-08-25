from dataclasses import replace
import os


def find_data():
    print('Введите имя файла: ')
    file_name = input()
    data = open(file_name + '.txt', 'r', encoding='utf-8')
    for line in data:
        print(line)
    data.close()


def new_data():
    print('Введите название нового файла: ')
    new_file_name = str(input())
    data = open(new_file_name + '.txt', 'w', encoding='utf-8')
    print('Введите ФИО и номер телефона(+7) через пробел: ')
    original_data = input()
    data.write(original_data)
    data.close()


def correction_data():
    print('Введите имя файла: ')
    file_name = input()
    data = open(file_name + '.txt', 'r', encoding='utf-8')
    print(data.read())
    data.close()

    data = open(file_name + '.txt', 'w', encoding='utf-8')
    print('Введите НОВЫЕ! ФИО и номер телефона(+7) через пробел: ')
    original_data = input()
    data.write(original_data)
    data.close()
    

def delete_data():
    print('Введите имя файла который хотите удалить: ')
    file_name = input()
    data = open(file_name + '.txt', 'r', encoding='utf-8')
    print(data.read())
    data.close()
    os.remove(file_name + '.txt')
    

def change_data():
    print('Введите имя файла который хотите изменить: ')
    file_name = input()
    data = open(file_name + '.txt', 'r', encoding='utf-8')
    print(data.read())
    data.close()

    answer = int(input('Какие данные Вы хотите поменять?\n'
                       '1 - Фамилия\n'
                       '2 - Имя\n'
                       '3 - Отчество\n'
                       '4 - Телефон\n'
                       "Введите ответ: "))
    
    while True:   
        if answer not in [1, 2, 3, 4]:
            print('Ошибочный запрос!')
        elif answer == 1:
            change_data_in_file(file_name, answer-1)
            return
        elif answer == 2:
            change_data_in_file(file_name, answer-1)
            return
        elif answer == 3:
            change_data_in_file(file_name, answer-1)
            return
        elif answer == 4:
            change_data_in_file(file_name, answer-1)
            return

def change_data_in_file(file_name, indx):
    data = open(file_name + '.txt', 'r', encoding='utf-8')
    old_data = data.read()
    list = old_data.replace("\n", " ").split(" ")
    print('Введите новые данные ')
    list[indx] = input()
    change_data = ' '.join(list)
    with open (file_name + '.txt', 'w', encoding='utf-8') as f:
        f.write(change_data)
    print("Данные в файле успешно изменены!")
    data.close()

    