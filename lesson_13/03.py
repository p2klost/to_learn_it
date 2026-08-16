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
from os import listdir, getcwd, PathLike
from os.path import join

dir = join(getcwd(),"lesson_13\\project")

def check_dir(directory: PathLike) -> str:
    txt_num = 0
    
    for i in listdir(directory):
        if i.endswith(".txt"):
            print(i[0:len(i)-4]) # чтобы убрать .txt и вывести только имя файла
            txt_num += 1

    return txt_num

print(check_dir(dir)) # выводит (принтует) имена и возвращает кол-во
