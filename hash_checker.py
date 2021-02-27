import os
import hashlib
import sys
from threading import Thread, BoundedSemaphore

threadLimiter = BoundedSemaphore(1000)
#   class of thread for check hash-sum / класс потока для проверки хэш-суммы
class CheckingThread(Thread):
    def __init__(self, file_path, hash_func, file_hash):
        self.file_path = file_path
        self.hash_func = hash_func
        self.file_hash = file_hash

    def run(self):
        threadLimiter.acquire()
        try:
            if self.hash_func == 'sha1':
                sha1_check(self.file_path, self.file_hash)
            elif self.hash_func == 'sha256':
                sha256_check(self.file_path, self.file_hash)
            elif self.hash_func == 'md5':
                md5_check(self.file_path, self.file_hash)
            else:
                filename = self.file_path.split('\\')
                filename = filename[len(filename) - 1]
                print(f'{filename} FAIL')
        finally:
            threadLimiter.release()

#   read input file / считывание входящего файла
def read_input(filename, directory):
    files_list = os.listdir(directory)
    with open(filename, 'r') as file:
        strings = file.read().splitlines()
        for string in strings:
            string = string.split(' ')
            file_path = string[0]
            if file_path in files_list:
                file_path = directory + f'\{file_path}'
                hash_func = string[1]
                file_hash = string[2]
                thread = CheckingThread(file_path, hash_func, file_hash)
                thread.run()
            else:
                filename = file_path.split('\\')
                filename = filename[len(filename) - 1]
                print(f'{filename} NOT FOUND')

#   check hash-sum if encryption method sha1 / проверка хэш-суммы файла, sha1
def sha1_check(file_path, file_hash):
    hash_object = hashlib.sha1()
    filename = file_path.split('\\')
    filename = filename[len(filename) - 1]
    try:
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(1024), b''):
                hash_object.update(chunk)
    except:
        print(f'{filename} FAIL')
    if hash_object.hexdigest() != file_hash:
        print(f'{filename} FAIL')
    else:
        print(f'{filename} OK')

#   check hash-sum if encryption method sha256 / проверка хэш-суммы файла, sha256
def sha256_check(file_path, file_hash):
    hash_object = hashlib.sha256()
    filename = file_path.split('\\')
    filename = filename[len(filename) - 1]
    try:
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(1024), b''):
                hash_object.update(chunk)
    except:
        print(f'{filename} FAIL')
    if hash_object.hexdigest() != file_hash:
        print(f'{filename} FAIL')
    else:
        print(f'{filename} OK')

#   check hash-sum if encryption method md5 / проверка хэш-суммы файла, md5
def md5_check(file_path, file_hash):
    hash_object = hashlib.md5()
    filename = file_path.split('\\')
    filename = filename[len(filename) - 1]
    try:
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(1024), b''):
                hash_object.update(chunk)
    except:
        print(f'{filename} FAIL')
    if hash_object.hexdigest() != file_hash:
        print(f'{filename} FAIL')
    else:
        print(f'{filename} OK')

def main():
    input_file = sys.argv[1]
    directory = sys.argv[2]
    try:
        read_input(input_file, directory)
    except FileNotFoundError:
        print(f'"{directory}" FileNotFoundError')

if __name__ == '__main__':
    main()
