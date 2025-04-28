"""
1. Створення моделі даних: Створіть просту модель даних для системи управління студентами. Модель може містити
    таблиці для студентів, курсів та їх відношень. Кожен студент може бути зареєстрований на декілька курсів.
    Наприклад, створити 5 курсів, та розподілити рандомно 20 студентів.
2. Виконання базових операцій: Напишіть програму, яка додає нового студента до бази даних та додає його до
    певного курсу. Переконайтеся, що ці зміни коректно відображаються у базі даних.
3. Запити до бази даних: Напишіть запити до бази даних, які повертають інформацію про студентів, зареєстрованих
    на певний курс, або курси, на які зареєстрований певний студент.
4. Оновлення та видалення даних: Реалізуйте можливість оновлення даних про студентів або курси, а також
    видалення студентів з бази даних.
5. Можна використовувати будь яку ORM на Ваш вібир
"""

from sqlalchemy import create_engine, Column, Integer, String, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

DATABASE_URL = "sqlite:///homework_22.db"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

student_courses = Table(
    'student_courses',
    Base.metadata,
    Column('student_id', ForeignKey('students.id'), primary_key=True),
    Column('course_id', ForeignKey('courses.id'), primary_key=True)
)

class Students(Base):
    __tablename__ = 'students'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    surname = Column(String)
    age = Column(Integer)

    courses = relationship('Courses', secondary=student_courses, back_populates='students')

    def __str__(self):
        return f"Student ID: {self.id}, first_name: {self.first_name}, surname: {self.surname}, age: {self.age}"


class Courses(Base):
    __tablename__ = 'courses'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    lectures_count = Column(Integer)

    students = relationship('Students', secondary=student_courses, back_populates='courses')

    def __str__(self):
        return f"Course ID: {self.id}, Title: {self.title}, Lectures: {self.lectures_count}"

class DatabaseManager:
    def __init__(self, engine):
        Session = sessionmaker(bind=engine)
        self.session = Session()


    def create_tables(self):
        Base.metadata.create_all(engine)


    def add_records(self, records_list):
        self.session.add_all(records_list)
        self.session.commit()

    def assign_courses_by_ids(self, assignments: dict):
        students = {student.id: student for student in self.session.query(Students).all()}
        courses = {course.id: course for course in self.session.query(Courses).all()}

        for student_id, course_ids in assignments.items():
            if student_id in students:
                selected_student = students[student_id]
                selected_student.courses = [courses[c_id] for c_id in course_ids if c_id in courses]
        self.session.commit()

    def get_all_records(self, model):
        records = self.session.query(model).all()
        if records:
            print(f"Данні з таблиці {model.__name__}:")
            for record in records:
                print(record)
        else:
            print(f"Записи в таблиці {model.__name__} не знайдені.")


    def get_records_by_relation(self, model, related_model, related_value):
        if model == Students and related_model == Courses:
            related_item = self.session.query(Courses).filter_by(title=related_value).first()
            if related_item:
                print(f"Список студентів записаних на курс '{related_value}':")
                for student in related_item.students:
                    print(f"{student.first_name} {student.surname}")
            else:
                print(f"Курс '{related_value}' не знайден.")

        elif model == Courses and related_model == Students:
            related_item = self.session.query(Students).filter_by(first_name=related_value[0],
                                                                  surname=related_value[1]).first()
            if related_item:
                print(f"Список курсів для студента {related_value[0]} {related_value[1]}:")
                for course in related_item.courses:
                    print(f"{course.title}")
            else:
                print(f"Студент {related_value[0]} {related_value[1]} не знайден.")


    def update_record(self, model, record_id, **kwargs):
        record = self.session.query(model).filter_by(id=record_id).first()
        if record:
            for key, value in kwargs.items():
                if hasattr(record, key):
                    setattr(record, key, value)
            self.session.commit()
        else:
            print(f"{model.__name__} з ID {record_id} не знайден.")


    def change_relation(self, student_id, course_id, action="add"):
        student = self.session.query(Students).filter_by(id=student_id).first()
        course = self.session.query(Courses).filter_by(id=course_id).first()

        if student and course:
            if action == "add":
                if course not in student.courses:
                    student.courses.append(course)
                    self.session.commit()
                else:
                    print(f"Cтудент {student.first_name} {student.surname} вже займається на курсі '{course.title}'.")
            elif action == "remove":
                if course in student.courses:
                    student.courses.remove(course)
                    self.session.commit()
                else:
                    print(f"Студент {student.first_name} {student.surname} не займається на курсі '{course.title}'.")
        else:
            print("Студент чи курс не знайден.")


    def clear_records(self, model, filter_conditions=None):
        query = self.session.query(model)
        if filter_conditions:
            query = query.filter_by(**filter_conditions)
        query.delete()
        self.session.commit()


if __name__ == "__main__":
    db = DatabaseManager(engine)

    # Завдання №1-2
    db.create_tables()
    db.add_records([
        Students(first_name='John', surname='Snow', age=30),
        Students(first_name='Alice', surname='Frost', age=25),
        Students(first_name='Bob', surname='Tiger', age=35),
        Students(first_name='Luna', surname='Rivera', age=28),
        Students(first_name='Mark', surname='Steel', age=40),
        Students(first_name='Emily', surname='Dawn', age=22),
        Students(first_name='Jack', surname='Stone', age=31),
        Students(first_name='Nina', surname='Woods', age=29),
        Students(first_name='Oscar', surname='Blaze', age=33),
        Students(first_name='Grace', surname='Knight', age=26),
        Students(first_name='Ethan', surname='Wolf', age=37),
        Students(first_name='Chloe', surname='Fox', age=24),
        Students(first_name='Leo', surname='Frost', age=32),
        Students(first_name='Mia', surname='Storm', age=27),
        Students(first_name='Ivan', surname='Flint', age=38),
        Students(first_name='Zoe', surname='Skye', age=23),
        Students(first_name='Ryan', surname='Grimm', age=34),
        Students(first_name='Ella', surname='Hawk', age=30),
        Students(first_name='Dylan', surname='North', age=36),
        Students(first_name='Sophie', surname='Vale', age=21),
    ])
    db.add_records([
        Courses(title='QA Automation', lectures_count=40),
        Courses(title='Python basic', lectures_count=32),
        Courses(title='Data Analyst', lectures_count=38),
        Courses(title='QA starter', lectures_count=45),
        Courses(title='Project management', lectures_count=65)
    ])

    assignments_by_ids = {
        1: [1, 2],
        3: [2, 3, 4],
        5: [1, 4],
        10: [2, 5],
    }
    db.assign_courses_by_ids(assignments_by_ids)

    # Завдання №3
    db.get_records_by_relation(Students, Courses, 'QA Automation')
    db.get_records_by_relation(Courses, Students, ('John', 'Snow'))


    # Завдання №4
    db.update_record(Students, 1, first_name="Johnathan")
    db.update_record(Courses, 1, title="Advanced QA Automation")
    db.change_relation(1, 3, "add")
    db.change_relation(1, 2, "remove")
    db.get_records_by_relation(Students, Courses, 'Advanced QA Automation')
    db.get_records_by_relation(Courses, Students, ('Johnathan', 'Snow'))

    db.clear_records(Students)
    db.clear_records(Courses, {'title':'QA starter'})
    db.get_all_records(Students)
    db.get_all_records(Courses)
    db.clear_records(Courses)