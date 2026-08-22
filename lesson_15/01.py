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

    def __init__(self, name: str):
        self.name = name
        self.course_grades = {}


    def avg_grade(self):
        return sum(self.grades) / len(self.grades)

    def add_course(self,new_course):
        if self.grades is None:
            self.grades = list()
        return self.grades.append(new_course)

    