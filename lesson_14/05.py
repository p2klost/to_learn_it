"""
Есть файл users.csv: 
name,email,phone 
Alex,alex@example.com,+375291234567 
Maria,maria@test.by,+375441112233 
John,john@example,+375123 
Anna,anna@gmail.com,+375297778899 
 
Программа должна: 
●  прочитать CSV; 
●  проверить каждый email с помощью регулярного 
выражения; 
●  проверить телефон; 
●  вывести пользователей с некорректными данными. 
"""

import csv
import re

with open(r"lesson_14\05\01.csv","r",encoding="utf-8") as file:
    rfile = csv.reader(file)
    next(rfile)

    for i in rfile:
        if re.fullmatch(r"\S+\@\S+\.\S+",i[1]) is None:
            print(f"У пользователя {i[0]} некорректный email.")
        if re.fullmatch(r"\+375(29|33|44|25)\d{7}",i[2]) is None:
            print(f"У пользователя {i[0]} некорректный телефон.")
