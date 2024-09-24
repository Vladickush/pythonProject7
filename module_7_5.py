# Задание по теме "Файлы в операционной системе".
import os
import time

"""Методы операционной системы:
os.walk,
os.path.join
os.path.getmtime
os.path.dirname
os.path.getsize
"""

directory = r'C:\Users\HP\PycharmProjects\pythonProject7\second'
for root, dirs, files in os.walk(directory):
    for file in files:
        filepath = os.path.join(directory)
        filetime = os.path.getmtime(file)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime())
        filesize = os.path.getsize(file)
        parent_dir = os.path.dirname(root)

        print(f'Обнаружен файл: {file}')
        print(f'Путь: {filepath}')
        print(f'Время изменения: {formatted_time}, ')
        print(f'Размер: {filesize} байт, ')
        print(f'Родительская директория: {parent_dir}')
