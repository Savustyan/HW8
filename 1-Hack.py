import string
import random
import zipfile
import sys
from zipfile import ZipFile

PASSWORD_LENGTH = 4


def extract_archive(file_to_open, password):
    """
    Функция открывает архив с паролем и возвращает результат операции (bool)
    """
    try:
        zf = zipfile.ZipFile(file_to_open)
        zf.extractall(pwd=password.encode())
        # file_to_open.extractall(pwd=password.encode()) - don't work
        return True
    except Exception as e:
        print(e)
        return False


def build_pass():
    empty = ''
    for _ in range(PASSWORD_LENGTH):
        empty += random.choice(string.digits)
    return empty


def hack_archive(file_name):
    """
    Функция брутфорсит запароленный архив
    """
    file_to_open = zipfile.ZipFile(file_name)  # объект архива
    wrong_passwords = []  # список паролей, которые не подошли
    tries = 0  # колличество неудачных попыток

    while True:
        password = build_pass()
        print(password)
        if password not in wrong_passwords:
            if not extract_archive(file_name, password):
                wrong_passwords.append(password)
                tries += 1
            else:
                print(f'Archive {file_name} is hacked. Password - {password}')
                print(f'Password was found after {tries} tries')
                sys.exit(0)

filename = 'task.zip'
hack_archive(filename)


