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

directory = '.'   
for root, dirs, files in os.walk(directory):

    for file in files:
        filepath = os.path.join(root,file)
        filetime = os.path.getmtime(filepath)
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime())
        filesize = os.path.getsize(filepath)
        parent_dir = os.path.dirname(filepath)

        print(f'Обнаружен файл: {file}')
        print(f'Путь: {filepath}')
        print(f'Время изменения: {formatted_time}, ')
        print(f'Размер: {filesize} байт, ')
        print(f'Родительская директория: {parent_dir}')
        print()
