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
    contacts_list.append((re.sub(pattern, r'\1\3\10\4\6\9\7\8', ','.join(items))).split(','))

pprint(contacts_list)
print('=======================================================================')
list_cont = list()
for i in contacts_list:
    if i not in list_cont:
        
        list_cont.append(i)

print('---------------------------------------------------------------------')
pprint(list_cont)
# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#     # Вместо contacts_list подставьте свой список
#     datawriter.writerows(contacts_list)
