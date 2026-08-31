"""
Разработайте класс Student, который хранит информацию о 
студенте: имя, список курсов и оценки. Реализуйте методы 
для расчета среднего балла и добавления новых курсов. 
Создайте группу студентов и найдите студента с лучшей 
успеваемостью 
Добавьте метод для вывода информации о незавершенных 
курсах 
Реализуйте функцию, которая формирует список отличников 
"""

class Student:

    def __init__(self, name: str, courses_grades: list[tuple[str, int | float]]) -> None:
        self.student = {}
        self.student["name"] = name
        self.student["courses_grades"] = courses_grades # решил сделать лист с кортежами, чтобы было соответствие "курс, оценка"

    @property
    def avg_grade(self) -> float:
        sum_num = None
        len_num = None
        for i in self.student["courses_grades"]:
            if isinstance(i,str):
                continue
            else:
                sum_num = i[1] if sum_num is None else sum_num + i[1]
                len_num = 1 if len_num is None else len_num + 1
        return float(f"{(sum_num / len_num):.2f}")

    @property
    def incomplete_info(self) -> None:
        incomplete_list = list()
        for i in self.student["courses_grades"]:
            if isinstance(i,str):
                incomplete_list.append(i)
            else:
                continue
        return incomplete_list
    
    def add_course(self,course: str, grade: int | None = None) -> None:
        for i in self.student["courses_grades"]:
            if course in i:
                return print("Курс уже есть в списке. Курс не добавлен.")
            if grade is not None:
                if grade > 10:
                    return print("Оценка курса не может быть больше 10. Курс не добавлен.")
        return self.student["courses_grades"].append((course)) if grade is None else self.student["courses_grades"].append((course, grade))

def check(*args, best: bool = False) -> list | str: # best=True - даст лучшего из всех (одного или список, если одинаковый средний балл у нескольких), best=False - просто список отличников
    good_students = list()
    best_student = list()
    best_grade = None
    
    for i in args:
        if i.avg_grade >= 7:
            good_students.append(i.student["name"])        
        if best_grade is None:
            best_grade = i.avg_grade
        if i.avg_grade == best_grade:
            best_student.append(i.student["name"])   
        if i.avg_grade > best_grade:
            best_grade = i.avg_grade
            del best_student[0]
            best_student.append(i.student["name"])

    if best is False:
        return good_students

    if best is True and len(best_student) == 1: # если одинаковые оценки у нескольких студентов, то список таких студентов
        return best_student[0]
    else:
        return best_student

student1 = Student("Nikita",[("math",9), ("chemistry",3), ("physics",7)])
student2 = Student("Pavel",[("engineering",7), ("chemistry",5), ("biology",8)])
student3 = Student("Masha",[("marketing",5), ("sociology",8), ("economics",8)])
print(student1.avg_grade) # средняя по всем курсам у Никиты
print(student2.avg_grade) # средняя по всем курсам у Павла
print(student3.avg_grade) # средняя по всем курсам у Маши
student1.add_course("biology",9.8) # добавление "курс, оценка"
student2.add_course("chemistry",8) # курс уже есть в списке, возвращается сообщение о том что курс уже есть. Курс не добавлен.
student1.add_course("math") # курс уже есть в списке, возвращается сообщение о том что курс уже есть. Курс не добавлен.
student1.add_course("engineering",12.2) # оценка больше 10, возвращается сообщение о том что оценка не может быть > 10. Курс не добавлен.
student1.add_course("economics") # добавление "курс", без оценки - значит он еще незавершен
student1.add_course("sociology") # добавление "курс", без оценки - значит он еще незавершен
print(student1.student)
print(student1.avg_grade) # средняя Никиты после добавления новых курсов
print(student1.incomplete_info) # список незавершенных курсов у Никиты
print(check(student1,student2,student3,best=True)) # лучший из всех
print(check(student1,student2,student3,best=False)) # список отличников (если средний >= 7 )