# Дан список 
# files = [ 
#     "main.py", 
#     "test.py", 
#     "README.md", 
#     "data.csv", 
#     "notes.txt" 
# ] 
# Оставьте только Python-файлы. 
# Используйте filter. 

files = [ 
    "main.py", 
    "test.py", 
    "README.md", 
    "data.csv", 
    "notes.txt" 
] 

files = list(filter(lambda x: True if ".py" in x else False,files))
# print(files)
