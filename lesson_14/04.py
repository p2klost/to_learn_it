"""
Содержимое: 
name,price,category 
Laptop,1200,Electronics 
Phone,800,Electronics 
Book,25,Books 
Table,300,Furniture 
 
Напишите программу, которая: 
●  читает CSV; 
●  выводит названия всех товаров; 
●  находит товары дороже 500; 
●  считает их количество; 
●  выводит самый дорогой товар. 
"""

import csv

with open(r"lesson_14\04\01.csv","r",encoding="utf-8") as file:
    rfile_list = list(csv.DictReader(file))
    max_price = rfile_list[0]
    expensive = 0

    print("Названия всех товаров:")
    for i in rfile_list:
        print(i["name"])
        if int(i["price"]) > int(max_price["price"]):
            max_price = i
        if int(i["price"]) > 500:
            expensive += 1
    print("Кол-во товаров дороже 500:",expensive)      
    print(f"Самый дорогой товар: {max_price["name"]}. Цена: {max_price["price"]}")





