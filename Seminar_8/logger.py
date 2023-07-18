from data_create import input_user_data

def input_data():
    name, surname, phone, adress = input_user_data()
    print(name, surname, phone, adress)
    var = int(input(f'В каком виде записать данные?\n'
                    f'1 Вариант: \n'
                    f'{name}\n'
                    f'{surname}\n'
                    f'{phone}\n'
                    f'{adress}\n\n'
                    f'2 Вариант: \n'
                    f'{name};{surname};{phone};{adress}\n\n'
                    f'Ваш выбор: '))
    
    while var < 1 or var > 2:
        var = int(input('Ошибка! Попробуй еще раз! Ваш выбор: '))
    
    if var == 1:
        with open('Seminar_8\data_first_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name}\n'
                       f'{surname}\n'
                       f'{phone}\n'
                       f'{adress}\n\n')
    else:
        with open('Seminar_8\data_second_variant.csv', 'a', encoding='utf-8') as file:
            file.write(f'{name};{surname};{phone};{adress}\n\n')
    print('Данные добавленны в {var} файл')  
        

def print_data():
    print('1 файл: ')
    with open('Seminar_8\data_first_variant.csv', 'r', encoding='utf-8') as file:
        data = file.readlines()
        data_list = list()
        j = 0
        for i in range(len(data)):
            if data[i] == '\n':
                data_list.append(''.join(data[j:i]))
                j = i
        print(''.join(data_list))
    
    print('2 файл: ')
    with open('Seminar_8\data_second_variant.csv', 'r', encoding='utf-8') as file:
        data = list(file.readlines())
        print(''.join(data))

def delet_data():
    print('Содержимое телефонной книги:\n'
          'Имя; Фамили; Телефон; Адресс')
    with open('Seminar_8\data_3_variant.csv', 'r', encoding='utf-8') as file:
        lines = file.read().split('\n')
    for key, line in enumerate(lines):
        print(f'{key}: {line}')
    str_to_delete = int(input('Введите номер строки, которую нужно удалить: '))
    while str_to_delete > key:
        str_to_delete = int(input('Ошибка! Попробуй еще раз! Ваш выбор: '))
    del lines[str_to_delete]
    with open('Seminar_8\data_3_variant.csv', 'w', encoding='utf-8') as file:
        file.write('\n'.join(lines))
    print(f'\033[32mДанные успешно записаны!\033[0m')