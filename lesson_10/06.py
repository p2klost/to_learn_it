# Дан список студентов: 
# students = [ 
#     {"name": "Иван", "score": 82}, 
#     {"name": "Анна", "score": 95}, 
#     {"name": "Петр", "score": 67}, 
#     {"name": "Мария", "score": 91}, 
#     {"name": "Олег", "score": 73}, 
#     {"name": "Елена", "score": 88}, 
# ] 
# Используя функциональный стиль программирования: 
# 1.  оставить студентов, набравших не менее 80 баллов; 
# 2.  отсортировать их по убыванию результата; 
# 3.  получить список строк вида: 
# Анна (95) 
# Мария (91) 
# Елена (88) 
# Иван (82)

students = [ 
    {"name": "Иван", "score": 82}, 
    {"name": "Анна", "score": 95}, 
    {"name": "Петр", "score": 67}, 
    {"name": "Мария", "score": 91}, 
    {"name": "Олег", "score": 73}, 
    {"name": "Елена", "score": 88}] 

def scores(students: list) -> str:
    students_scores = list(filter(lambda x: True if x["score"] >= 80 else False,students))
    students_scores.sort(key=lambda x: x.get("score"))
    for i in students_scores[::-1]:
        print(f"{i["name"]} ({i["score"]})")

scores(students)