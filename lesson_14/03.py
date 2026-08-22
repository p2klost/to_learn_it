"""
Дана директория: 
 
project/ 
    data.txt 
    config.json 
    image.png 
    users.txt 
    README.md 
 
Напишите программу, которая с помощью os.listdir(): 
 
●  получает список содержимого директории; 
●  находит только файлы с расширением .txt; 
●  выводит их имена; 
●  считает их количество.
"""
from os import listdir, PathLike
from os.path import splitext


dir = r"lesson_14\03\project"

def check_dir(directory: PathLike) -> int:
    txt_num = 0
    
    for i in listdir(directory):
        if i.endswith(".txt"):
            print(splitext(i)[0])
            txt_num += 1
    
    return txt_num

print(check_dir(dir)) # функция выводит (принтует) имена и возвращает кол-во
