"""
Створіть клас "Студент" з атрибутами "ім'я", "прізвище", "вік" та "середній бал".
Створіть об'єкт цього класу, представляючи студента.
Потім додайте метод до класу "Студент", який дозволяє змінювати середній бал студента.
Виведіть інформацію про студента та змініть його середній бал.
"""

class Student:
    def __init__(self, name, surname, age, gpa):
        self.name = name
        self.surname = surname
        self.age = age
        self.gpa = gpa
    def student_presentation(self):
        return f'Привітайте {self.name} {self.surname}, якому виповнилося {self.age} років, ' \
               f'та який отримав середній бал {self.gpa} за минулий рік.'
    def gpa_changing(self, new_gpa):
        if new_gpa > 0:
            self.gpa = new_gpa
        else:
            print("Отриманний бал повинен бути більше 0!")