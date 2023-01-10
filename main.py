import re
from pprint import pprint
import csv

# читаем адресную книгу в формате CSV в список contacts_list

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
    my_list = []
    staff = {}
    for i in contacts_list:
        e_mail = i[-1]
        phone = re.sub(r'(\+7|8|8 )( |)(|\()(\d{3})(|\-)(|\))(| )(\d{3})(|\-)(\d{2})(|\-)(\d{2})', r'+7(\4)\8-\10-\12',
                       str(i[-2]))  # выделяю все телефоны (с добавочными и без), сохраняю в отдельной переменной
        phone_with_add_number = re.sub(r'(|\()(\w+)(\. )(\d+)(\)|)', r'\2.\4',
                                       phone)  # обрабатываю телефон в соответствии с шаблоном
        name_company_position_string = re.sub(
            r'\[\'(\w+)([ \'\,]+)(\w+)([ \'\,]+)(|\w+)([ \'\,]+)(|\w+)([ \'\,]+)(|([a-zА-Яа-я –]+))([ \'\,]+)(.+)',
            r'\1, \3, \5, \7, \10', str(i))  # сохраняю в отдельную переменную ФИО + компания + должность в виде строки

        name_company_position_made_list = name_company_position_string.split(', ')  # привожу строку в формат списка
        name_company_position_made_list.append(phone_with_add_number)  # добавляю к списку номер телефона
        name_company_position_made_list.append(e_mail)  # добавляю почту
        my_list.append(
            name_company_position_made_list)  # добавляю полученнный в итерации список в общий список контактов

    # прохожу по общему списку контактов, если нет такого контакта, то, добавляю в общий словарь, если есть, то делаю замены пустых строк
    for i in range(len(my_list)):
        if my_list[i][0] in staff:
            for y in range(len(staff[my_list[i][0]])):
                if len(staff[my_list[i][0]][y]) == 0:
                    staff[my_list[i][0]][y] = my_list[i][y + 1]
        else:
            staff[my_list[i][0]] = [my_list[i][1], my_list[i][2], my_list[i][3], my_list[i][4], my_list[i][5],
                                    my_list[i][6]]

# перевожу в формат списка
finifh_list = [(k, *v) for k, v in staff.items()]

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(finifh_list)
