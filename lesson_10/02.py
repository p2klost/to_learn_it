# words = [ 
#     "Python", 
#     "java", 
#     "C++", 
#     "Rust", 
#     "Go", 
#     "Swift", 
#     "PHP" 
# ] 
# Получите новый список, содержащий слова длиной не менее 
# пяти символов в нижнем регистре.

words = [ 
    "Python", 
    "java", 
    "C++", 
    "Rust", 
    "Go", 
    "Swift", 
    "PHP"] 

new_words = list()

for i in words:
    count = 0
    for a in i:
        if a.islower():
            count += 1
        if count == 5:
            new_words.append(i)

# print(new_words)