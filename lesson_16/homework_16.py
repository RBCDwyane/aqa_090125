"""
Завдання 1

Створіть клас **`Employee`**, який має атрибути **`name`** та **`salary`**.
Далі створіть два класи, **`Manager`** та **`Developer`**, які успадковуються від **`Employee`**.
Клас **`Manager`** повинен мати додатковий атрибут **`department`**, а клас **`Developer`** -
атрибут **`programming_language`**.

Тепер створіть клас **`TeamLead`**, який успадковується як від **`Manager`**, так і від **`Developer`**.
Цей клас представляє керівника з команди розробників. Клас **`TeamLead`** повинен мати всі атрибути як
**`Manager`** (ім'я, зарплата, відділ), а також атрибут **`team_size`**, який вказує на кількість розробників
у команді, якою керує керівник.

Напишіть тест, який перевіряє наявність атрібутів з `Manager` та `Developer` у класі `TeamLead`

Завдання 2

Створіть абстрактний клас "Фігура" з абстрактними методами для отримання площі та периметру.
Наслідуйте від нього декілька (> 2) інших фігур, та реалізуйте математично вірні для них методи
для площі та периметру. Властивості по типу “довжина сторони” й т.д. повинні бути приватними,
та ініціалізуватись через конструктор. Створіть Декілька різних об’єктів фігур, та у циклі 
порахуйте та виведіть в консоль площу та периметр кожної.

### Складність

Висока

# Як робити домашне завдання у Git

1. **ОБОВ’ЯЗКОВО с**творіть нову гілку, яка буде використовуватись для змін, за 
    допомогою команди `git checkout -b homework##`
2. **Виконайте ДЗ у окремому файлі homework_<#lesson>.py**
3. Зробіть коміт з змінами, додавши опис виконаних змін
4. Відправте свої зміни до вашого репозиторію 
5. Створіть pull request у  власну гілку `main` на головний репозиторію 
    [https://github.com](https://github.com/), натиснувши кнопку "New pull request" на
    відповідному розділі репозиторію.
6. Назначте ревьювером викладача
7. **Посилання на PR вставте у форму відповіді для ДЗ в навчальній системі**
"""

# 1st task
class Employe:
    def __init__(self, name, salary):
        if not isinstance(name, str):
            raise TypeError('параметр name повинен бути строкою')
        self.name = name
        if not isinstance(salary, int):
            raise TypeError('параметр salary повинен бути цiлим числом')
        self.salary = salary

class Manager(Employe):
    def __init__(self, name, salary, department):
        Employe.__init__(self, name, salary)
        if not isinstance(department, str):
            raise TypeError('параметр department повинен бути строкою')
        self.department = department

class Developer(Employe):
    def __init__(self, name, salary, programming_language):
        Employe.__init__(self, name, salary)
        if not isinstance(programming_language, str):
            raise TypeError('параметр programming_language повинен бути строкою')
        self.programming_language = programming_language

class TeamLead(Manager, Developer):
    def __init__(self, name, salary, department, programming_language, team_size):
        Manager.__init__(self, name, salary, department)
        Developer.__init__(self, name, salary, programming_language)
        if not isinstance(team_size, int):
            raise TypeError('параметр team_size повинен бути цiлим числом')
        self.team_size = team_size


# 2nd task
from abc import ABC, abstractmethod

class Figure(ABC):
    @abstractmethod
    def square(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        if not all(isinstance(side, (int, float)) for side in (side_a, side_b, side_c)):
            raise TypeError('Значення сторін повинно бути числом більше 0')
        if not all(side > 0 for side in (side_a, side_b, side_c)):
            raise ValueError('Значення сторін повинно бути числом більше 0')
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b  + side_c <= side_a:
            raise ValueError("Сума будь-яких двох сторін повинна бути більше третьої.")
        self._side_a = side_a
        self._side_b = side_b
        self._side_c = side_c

    def square(self):
        first = (self._side_a + self._side_b + self._side_c) / 2
        second = (first * (first - self._side_a) *
                       (first - self._side_b) * (first - self._side_c))
        return round(second, 2)
    def perimeter(self):
        return round((self._side_a + self._side_b + self._side_c), 2)

class Square(Figure):
    def __init__(self, side):
        if not isinstance(side, (int, float)):
            raise TypeError('Значення сторони повинно бути числом більше 0')
        if not side > 0 :
            raise ValueError('Значення сторони повинно бути числом більше 0')
        self._side = side

    def square(self):
        return round((self._side ** 2), 2)
    def perimeter(self):
        return round((self._side * 4), 2)

class Circle(Figure):
    Pi = 3.14159
    def __init__(self, radius):
        if not isinstance(radius, (int, float)):
            raise TypeError('Значення радіусу повинно бути числом більше 0')
        if not radius > 0 :
            raise ValueError('Значення радіусу повинно бути числом більше 0')
        self._radius = radius

    def square(self):
        return round((self._radius ** 2 * self.Pi), 2)
    def perimeter(self):
        return round((2 * self.Pi * self._radius), 2)

if __name__ == '__main__’:
    main()
triangle_1 = Triangle(2, 2, 3)
rectangle_1 = Square(5)
circle_1 = Circle(8)

figures = [triangle_1, rectangle_1, circle_1]
for i in figures:
    print(f'Площа {i.__class__.__name__}: {i.square()} та периметр: {i.perimeter()}')