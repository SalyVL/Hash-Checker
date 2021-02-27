import hashlib
import os
import sys
from random import randint
from threading import Thread, BoundedSemaphore

threadLimiter = BoundedSemaphore(1000)
class WriterThread(Thread):
    def __init__(self, file_path, rand):
        self.file_path = file_path
        self.rand = rand

    def run(self):
        threadLimiter.acquire()
        try:
            if self.rand == 1:
                sha1_write(self.file_path)
            elif self.rand == 2:
                sha256_write(self.file_path)
            else:
                md5_write(self.file_path)
        finally:
            threadLimiter.release()

def check_directory(directory):
    file_list = os.listdir(directory)
    for file in file_list:
        file_path = directory + f'\{file}'
        rand = randint(1,3)
        thread = WriterThread(file_path, rand)
        thread.run()

def sha1_write(filepath):
    hash_object = hashlib.sha1()
    try:
        with open(filepath, 'rb') as file:
            for chunk in iter(lambda: file.read(1024), b''):
                hash_object.update(chunk)
    except:
        pass
    hash_sum = hash_object.hexdigest()
    filename = filepath.split('\\')
    filename = filename[len(filename)-1]
    string = f'{filename} sha1 {hash_sum}\n'
    with open('writer_output.txt', 'a') as file:
        file.write(string)

def sha256_write(filepath):
    hash_object = hashlib.sha256()
    try:
        with open(filepath, 'rb') as file:
            for chunk in iter(lambda: file.read(1024), b''):
                hash_object.update(chunk)
    except:
        pass
    hash_sum = hash_object.hexdigest()
    filename = filepath.split('\\')
    filename = filename[len(filename)-1]
    string = f'{filename} sha256 {hash_sum}\n'
    with open('writer_output.txt', 'a') as file:
        file.write(string)

def md5_write(filepath):
    hash_object = hashlib.md5()
    try:
        with open(filepath, 'rb') as file:
            for chunk in iter(lambda: file.read(1024), b''):
                hash_object.update(chunk)
    except:
        pass
    hash_sum = hash_object.hexdigest()
    filename = filepath.split('\\')
    filename = filename[len(filename)-1]
    string = f'{filename} md5 {hash_sum}\n'
    with open('writer_output.txt', 'a') as file:
        file.write(string)

def main():
    directory = sys.argv[1]
    check_directory(directory)

if __name__ == '__main__':
    main()