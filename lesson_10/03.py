# Дана строка 
# text = "functional programming" 
# Создайте словарь, где ключ — символ, значение — количество 
# его появлений. 
# Пробелы учитывать не нужно.

text = "functional programming" 

new_dict = {i: text.count(i) for i in text.replace(" ", "")}
# print(new_dict)