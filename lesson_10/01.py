# Напишите рекурсивную функцию find_file(folder, 
# target_filename), которая ищет полный путь к 
# целевому файлу в словаре-дереве и возвращает строку с 
# путем или None. file_system = { 
#     "documents": { 
#         "work": { 
#             "project_notes.txt": "content", 
#             "budget.xlsx": "content" 
#         }, 
#         "personal": { 
#             "passport.pdf": "content" 
#         } 
#     }, 
#     "photos": { 
#         "vacation.jpg": "content" 
#     } 
# } 