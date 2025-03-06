"""
Створіть class SiteUser() для представлення користувача в системі.
Кожен користувач має ім'я, електронну пошту та рівень доступу (admin, moderator, user, blocked).
Також користувач має лічильник кількість логінів - logcount (int)
Реалізуйте необхідні методи та атрибути, використовуючи магічні методи для поліпшення
функціональності.

Вимоги:

    Клас Користувач має мати атрибути: ім'я, електронна_пошта, рівень_доступу, кількість логінів (logcount).
    Реалізуйте методи для отримання та встановлення значень атрибутів (гетери та сетери).
    Перевизначте метод __str__, щоб при виведенні об'єкта на екран 
    виводилася інформація про користувача.
    Реалізуйте метод __eq__, який дозволяє порівнювати два об'єкта за рівнем доступу.
    Реалізуйте щоб SiteUser.logcount можна було збільшувати

Приклад використання:

user1 = SiteUser("John Doe", "john.doe@example.com", "user")
user2 = SiteUser("Jane Smith", "jane.smith@example.com", "admin")

print(user1)
# Виведе: SiteUser: John Doe, mailbox: john.doe@example.com, access level: user

# Порівняння користувачів
if user1 == user2:
    print("Користувачі однакові")
else:
    print("Користувачі різні")

Написати на це все тести
"""

import json

class SiteUser:
    def __init__(self, name, email, access_level='user', logcount=0):
        if not isinstance(name, str) or not name:
            raise TypeError('Значення name повинно бути строкою.')
        self.name = name
        if not isinstance(email, str) or not email:
            raise TypeError('Значення email повинно бути строкою.')
        self.email = email
        if not isinstance(access_level, str):
            raise TypeError('Некоректне занчення  access level. Має бути одним з admin, moderator, user чи blocked.')
        if access_level not in ['admin', 'moderator', 'user', 'blocked']:
            raise ValueError('Некоректне занчення  access level. Має бути одним з admin, moderator, user чи blocked.')
        self.access_level = access_level
        if not isinstance(logcount, int):
            raise TypeError('Некоректне занчення  logcount. Має бути натуральним числом.')
        if logcount < 0:
            raise ValueError('Некоректне занчення  logcount. Має бути натуральним числом.')
        self._logcount = logcount

    def __str__(self):
        return json.dumps({'User': self.name, 'email': self.email, 'access level': self.access_level})
        #мені здалося, що так буде корректніше для потенційно подальшого використання класу.
        #також не додаю logcount, т.я. мені здалося з умов задачі, що його не потрібно виводити, а приховати

    def  __eq__(self, comparable):
        return isinstance(comparable, SiteUser) and self.email == comparable.email

    def get_logcount(self):
        return self._logcount
    def set_logcount(self, value):
        if not isinstance(value, int):
            raise TypeError('Некоректне занчення  logcount. Має бути натуральним числом.')
        if value < 0:
            raise ValueError('Некоректне занчення  logcount. Має бути натуральним числом.')
        self._logcount = value
    def add_logcount(self, value):
        if not isinstance(value, int):
            raise TypeError('Некоректне занчення  logcount. Має бути натуральним числом більше 0.')
        if value < 1:
            raise ValueError('Некоректне занчення  logcount. Має бути натуральним числом більше 0.')
        self._logcount += value

    def get_name(self):
        return self.name
    def set_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Значення name повинно бути строкою.')
        self.name = value

    def get_email(self):
        return self.email
    def set_email(self, value):
        if not isinstance(value, str):
            raise TypeError('Значення email повинно бути строкою.')
        self.email = value

    def get_access_level(self):
        return self.access_level
    def set_access_level(self, value):
        if value not in ['admin', 'moderator', 'user', 'blocked']:
            raise ValueError('Некоректне занчення  access level. Має бути одним з admin, moderator, user чи blocked.')
        self.access_level = value