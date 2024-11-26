# Task "Записать и запомнить"

from pprint import pprint

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

def custom_write(file_name, strings):
    elem = {}
    num = 0
    for i in info:
        file = open(file_name, 'a', encoding= 'utf-8')
        t = file.tell()
        num += 1
        file.write(f'{i}\n')
        elem.update({(num, t) : i})
        file.close()
    return elem


result = custom_write('list_strings.txt', info)

for elem in result.items():
    print(elem)

