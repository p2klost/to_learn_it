"""
Есть файл data.txt 
 
Напишите программу, которая: 
●  проверяет существование файла с помощью 
os.path.exists(); 
●  если файла нет — выводит сообщение; 
●  если файл существует — читает его; 
●  создаёт директорию backup если её ещё нет; 
●  создаёт backup/data.txt 
 
записывает туда содержимое исходного файла. 
"""
from os.path import exists, join, dirname, isdir
from os import mkdir

data = r"lesson_14\02\data.txt"
backup_path = join(dirname(data),"backup")
new_data = join(backup_path,"data.txt")

if exists(data):
    with open(data,"r",encoding="utf-8") as file:
            data_list = file.readlines()
    
    if not isdir(backup_path):
        mkdir(backup_path)
        
    with open(new_data,"w",encoding="utf-8") as file2:
        for i in data_list:
            file2.write(i)
else:
    print("Файла не существует.")