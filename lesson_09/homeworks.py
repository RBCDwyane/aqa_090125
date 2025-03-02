
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""

def multiplication_table(number=None):
    if number is None or not isinstance(number, int):
        raise TypeError("The input must be a positive integer.")
    if number < 1:
        raise ValueError("The input must be a positive integer.")
    table = []
    multiplier = 1
    while True:
        result = number * multiplier
        if  result > 25:
            break
        table.append(str(number) + "x" + str(multiplier) + "=" + str(result))
        multiplier += 1
    return table

"""  Написати функцію, яка розрахує середнє арифметичне списку чисел."""

def list_avg(lister=None):
    if lister is None or not isinstance(lister, list):
        raise TypeError("The input must be a list of numbers.")
    sum_list = 0
    count = 0
    for x in lister:
        if not isinstance(x, (float, int)):
            raise TypeError("The input list must include a integer or float numbers.")
        sum_list += x
        count += 1
    avg_list = sum_list / count
    return avg_list

"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def string_reverse(string=None):
    if string is None or not isinstance(string, str) or not string:
        raise TypeError("The input must be string.")
    return ''.join(reversed(string))

"""Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1.
Данні в лісті можуть бути будь якими
Перевірте, що репозиторій в git є публічним або ваш вчитель доданий до цього репозиторію.
Ви можете перевірити це в інкогніто-режимі вашого браузера.
Просто вставте посилання на свій репозиторій та переконайтеся, що ви можете побачити код."""

def str_filtering(input_list=None):
    if input_list is None or not isinstance(input_list, list) or not input_list:
        return "The input must be not empty list."
    filtered_list = [x for x in input_list if isinstance(x, str)]
    return filtered_list


"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""
def sum_of_digits(number=None):
    if not isinstance(number, int) or number <= 0 or not number:
        return "Input must be a natural number"
    return f'The sum of the digits of the number will be {sum(int(digit) for digit in str(number))}'
