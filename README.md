hash_checker.py 
Предназначен для проверки предоставленных хэш-сумм файлов. Принимает: файл с хэш-суммами файлов, каталог с файлами. Пробегается по каждой строчке файла с хэш-суммами и выводит результат проверки.
Принимает формат из командной строки: python hash_checker.py <файл с хэш-суммами> <каталог с файлами, которым принадлежат хэш-суммы>
Формат строк файла с хэш функциями: <имя файла> <метод шифрования (sha1/sha256/md5)> <хэш-сумма>

Пример строк: 
libxslt.dll sha256 fc9da6505d670c36d780578cf6a0b76912e594282d62fcee49790f65baaed2eb
oid2name.exe md5 e9dcfa5d4c880b40f2362a6f668908f4
pgbench.exe sha1 42c8e3067d59cd8ae7d961a050a82c29621d0ec1

Пример использования программы: 
cmd: python hash_checker.py C:\Users\vladi\Desktop\hash_checker\writer_output.txt D:\PostgreSQL\bin
Вывод: 
clusterb.exe NOT FOUND
createdb.exe FAIL
createuser.exe OK
dropdb.exe OK
dropuser.exe OK
ecpg.exe FAIL
icudt67.dll OK
icuin67.dll FAIL
icuio67.dll OK
icutu67.dll OK
icuuc67.dll OK
initdb.exe OK
isolationtester.exe OK
libcrypto-1_1-x64.dll OK
libcurl.dll OK
...

hash_writer.py 
Написан для тестирования hash_checker.py. Принимает: дирректорию с файлами. Рассчитывает хэш-сумму каждого файла случайным шифром (sha1/sha256/md5) и записывает в writer_output.txt.
Принимает формат из командной строки: python hash_writer.py <дирректория с файлами, хэш-суммы которых нужно записать>

Пример использования программы:
cmd: python hash_writer.py D:\PostgreSQL\bin
Вывод в файл writer_output.txt: 
pg_rewind.exe sha1 60bc680c64e44030b8634227c71091dbd1a15420
pg_standby.exe sha256 ca7690694b2b3cd316bbe91d43c088b0a2522d58d25dc92a154932ebebeb6602
pg_test_fsync.exe md5 3b5eeffc90e5cd850f87e06cfb0ba129
...