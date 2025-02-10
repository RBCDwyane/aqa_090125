
print('task 1')
""" Задача - надрукувати табличку множення на задане число, але
лише до максимального значення для добутку - 25.
Код майже готовий, треба знайти помилки та випраавити\доповнити.
"""
def multiplication_table(number):
    # Initialize the appropriate variable
    multiplier = 1

    # Complete the while loop condition.
    while True:
        result = number * multiplier
        # десь тут помила, а може не одна
        if  result > 25:
            # Enter the action to take if the result is greater than 25
            break
        print(str(number) + "x" + str(multiplier) + "=" + str(result))

        # Increment the appropriate variable
        multiplier += 1

multiplication_table(3)
# Should print:
# 3x1=3
# 3x2=6
# 3x3=9
# 3x4=12
# 3x5=15
print()

print('task 2')
"""  Написати функцію, яка обчислює суму двох чисел.
"""
def summa(a, b):
    c = a + b
    return c
print(summa(2, 2))
print()

print('task 3')
"""  Написати функцію, яка розрахує середнє арифметичне списку чисел.
"""
def list_avg(list):
    sum_list = 0
    count = 0
    for x in list:
        sum_list += x
        count += 1
    avg_list = sum_list / count
    return avg_list
print(list_avg([1, 2, 3, 4, 5]))
print()

print('task 4')
"""  Написати функцію, яка приймає рядок та повертає його у зворотному порядку.
"""
def string_reverse(string):
    rev_list = []
    for i in string[::-1]:
        rev_list.append(i)
    return rev_list
print(string_reverse([1, 2, 3, 4, 5]))
print()

print('task 5')
"""  Написати функцію, яка приймає список слів та повертає найдовше слово у списку.
"""
def max_word(words):
    max_word = max(words, key=len)
    return max_word
print(max_word(['potato', 'grape', 'watermellon']))
print()

print('task 6')
"""  Написати функцію, яка приймає два рядки та повертає індекс першого входження другого рядка
у перший рядок, якщо другий рядок є підрядком першого рядка, та -1, якщо другий рядок
не є підрядком першого рядка."""
def find_substring(str1, str2):
    result = str1.find(str2)
    return result

str1 = "Hello, world!"
str2 = "world"
print(find_substring(str1, str2)) # поверне 7

str1 = "The quick brown fox jumps over the lazy dog"
str2 = "cat"
print(find_substring(str1, str2)) # поверне -1
print()

"""  Оберіть будь-які 4 таски з попередніх домашніх робіт та
перетворіть їх у 4 функції, що отримують значення та повертають результат.
Обоязково документуйте функції та дайте зрозумілі імена змінним.
"""
print('task 7')
# Перевірте, чи є в списку big_list дублікати
def dubcat_detect(arg):
    result = len(arg) - len(set(arg))
    return result
print(f'у списку знаходиться {dubcat_detect([3, 5, 2, -1, -3, 0, 1, 4, 5, 2])} дублікати')
print()

print('task 8')
# Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
def filter_dict(input):
    final_dict = {}
    for name, age in dict(input).items():
        age_group = f"{age // 10 * 10}-{age // 10 * 10 + 9}"
        final_dict.setdefault(age_group, []).append(name)
    return final_dict

person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
print(filter_dict(person_list))
print()

print('task 9')
"""Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" 
(враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
Перевірте, що репозиторій в git є публічним або ваш вчитель доданий до цього репозиторію.
Ви можете перевірити це в інкогніто-режимі вашого браузера.
Просто вставте посилання на свій репозиторій та переконайтеся, що ви можете побачити код."""
def words_detect():
    while True:
        input_phrase = input('Write any word that contains the letter "h".')
        if 'h' in input_phrase or 'H'in input_phrase:
            return print(f"Thanks, for  your word '{input_phrase}'")
        else:
            print("Please, enter word with the 'h' letter. ")
words_detect()
print()

print('task 10')
"""Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. 
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. 
Данні в лісті можуть бути будь якими
Перевірте, що репозиторій в git є публічним або ваш вчитель доданий до цього репозиторію.
Ви можете перевірити це в інкогніто-режимі вашого браузера.
Просто вставте посилання на свій репозиторій та переконайтеся, що ви можете побачити код."""
def str_filtering(input_list):
    filtered_list = [x for x in input_list if isinstance(x, str)]
    return filtered_list

lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
print(str_filtering(lst1))