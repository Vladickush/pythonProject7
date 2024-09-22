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
        filepath = os.path.join
        filetime = os.path.getmtime
        formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(1))
        filesize = os.path.getsize
        parent_dir = os.path.dirname
print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')
