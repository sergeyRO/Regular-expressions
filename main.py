from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
contacts_list_modify = list()
for item in contacts_list:
    pattern = r"(\+7|8)(\s|\()*(\()*(\d{3})(\s|\))*(\s|\-)*(\d{3})(\s|\-)*(\d{2})(\s|\-)*(\d{2})(\(|\s)*(\(|\s)*(доб.)*(\s)*(\d+)*(\s|\))*"
    contacts_list_modify.append((re.sub(pattern, r'+7(\4)\7-\9-\11\15\14\16', ','.join(item))).split(','))

contacts_list = list()
for items in contacts_list_modify:
    pattern = r'^([А-ЯЁа-яё]*)(\s*)(\,?)([А-ЯЁа-яё]*)(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
    person = (re.sub(pattern, r'\1\3\10\4\6\9\7\8', ','.join(items))).split(',')
    del person[7:]
    contacts_list.append(person)

for a in contacts_list:
    for b in contacts_list:
        if a[0] == b[0]:
            if a is not b:
                if a[1] == '':
                    a[1] = b[1]
                if a[2] == '':
                    a[2] = b[2]
                if a[3] == '':
                    a[3] = b[3]
                if a[4] == '':
                    a[4] = b[4]
                if a[5] == '':
                    a[5] = b[5]
                if a[6] == '':
                    a[6] = b[6]

l=list()
for i in contacts_list:
    if i not in l:
        l.append(i)

contacts_list = l

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list)
