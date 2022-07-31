from pprint import pprint
import re
# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код
print(f'/n/n/n/n//n/n')
i = 0
contacts_list_modify = list()
for item in contacts_list:
    if i == 0:
        contacts_list_modify.append(item)
    else:
        contacts_list_modify.append(item)
        pattern = r"(\+7|8)(\s|\()?(\()?(\d{3})(\s|\))?(\s|\-)?(\d{3})(\s|\-)?(\d{2})(\s|\-)?(\d{2})"
        st = item
        contacts_list_modify.append(re.sub(pattern, r"+7(\4)\7 -\9 -\11", st))

        # pattern = r'(\+7|8)(\s|\()?(\()?(\d{3})(\s|\))?(\s|\-)?(\d{3})(\s|\-)?(\d{2})(\s|\-)?(\d{2})(\(|\s)?(\(|\s)?(доб.)(\s|)?(\d+)(\s|\))?'
        # replace1 = r'+7(\4)\7 -\9 -\11 \14\16'
        # print(re.sub(pattern, replace1, string))
    i += 1
print(contacts_list_modify)
# # TODO 2: сохраните получившиеся данные в другой файл
# # код для записи файла в формате CSV
# with open("phonebook.csv", "w") as f:
#     datawriter = csv.writer(f, delimiter=',')
#     # Вместо contacts_list подставьте свой список
#     datawriter.writerows(contacts_list)

string = 'foo42buz'
pattern = re.compile(r'(\d+)buz')
print(re.sub(pattern,'bar',string))