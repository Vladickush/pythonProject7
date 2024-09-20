# Задача "Записать и запомнить":

def custom_write(file_name, strings):
    dict_strings = {}
    number_string = 0
    file = open(file_name, 'a', encoding='utf-8')           #открытие файла 'test.txt'
    for string in strings:
        number_string += 1
        cursor = file.tell()
        dict_strings[(number_string, cursor)] = string      #запись в словарь dict_strings
        file.write(string + '\n')                           #запись в файл 'test.txt'
    file.close()
    return dict_strings


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
