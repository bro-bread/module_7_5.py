import os
import time

# Дирикторий
directory = "."


def explore_directory():
    # Обход каталогов
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Формируем путь к файлу
            filepath = os.path.join(root, file)

            # Получаем время изм файла
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))

            # Размер файла
            filesize = os.path.getsize(filepath)

            # родительскую директория
            parent_dir = os.path.dirname(filepath)

            # инфа о файле
            print(
                f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

