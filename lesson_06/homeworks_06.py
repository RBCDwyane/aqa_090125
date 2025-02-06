print('task 1')
"""  Уявіть, що інопланетянина з кольором alien_color щойно збили в грі.
Створіть змінну під назвою alien_color і призначте їй значення 'green', 'yellow', або 'red'.
Напишіть оператор if, щоб перевірити, чи колір прибульця 'green'.
Якщо так, надрукуйте повідомлення про те, що гравець щойно заробив 5 балів.
"""
alien_color = 'green'
if alien_color == 'green':
    print('Congrats, you archived 5 points!')
print()

print('task 2')
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою else.
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Зробіть так, щоб виводилася умова else.
"""
alien_color = 'red'
if alien_color == 'green':
    print('Congrats, you archived 5 points!')
else:
    print('Not bad! You archived 10 points!')
print()

print('task 3')
print('Hello, Earth! :)')
print()

print('task 4')
"""  Скопіюйте пеопередню відповідь, змініть і доповніть її умовою elif.
змінну під назвою alien_color перетворіть у список значень: 'green', 'yellow', 'red'
Якщо колір прибульця зелений, надрукуйте, що гравець щойно заробив 5 балів.
Якщо колір прибульця не зелений, надрукуйте, що гравець щойно заробив 10 балів.
Якщо прибулець червоний, надрукуйте повідомлення про те, що гравець заробив 15 очок
+ напишіть цикл for що перебере і обробить всі значення списку alien_color
"""
alien_color = ['green', 'yellow', 'red']
for i in alien_color:
    if i == 'green':
        print('Congrats, you archived 5 points!')
    elif i == 'red':
        print('Great! You archived 15 points!')
    else:
        print('Not bad! You archived 10 points!')
print()

print('task 5')
"""  Начинки для піци (pizza_topping): напишіть цикл, який пропонує користувачеві ввести ряд начинок
для піци, доки він не введе значення 'quit'. Коли вони введуть кожну начинку,
надрукуйте повідомлення про те, що ви додасте цю начинку до їхньої піци.
"""
pizza_topping = ['cheese', 'bacon', 'ham', 'olives', 'tomato', 'pepper', 'salami']
final_additives = []
print('Below you will be asked to choose additional pizza toppings. Please answer \'yes\', '
      '\'no\' or \'quit\' if you do not want anything.')
for i in pizza_topping:
    while True:
        additive = input(f'Would you like to add {i}? ').strip().lower()
        if additive == 'quit':
            break
        if additive == 'yes':
            final_additives.append(i)
            break
        elif additive == 'no':
            break
        else:
            print(f'please enter \'yes\', \'no\' or \'quit\'')
    if additive == 'quit':
        break
print('You ordered a standard pizza without any additives.' if not final_additives else
      f'You ordered a pizza with the following additives: {final_additives}')
input('See you later! press enter')
print()

print('task 6')
"""  Напишіть програму, яка знаходить суму всіх цифр натурального числа, яке вводить користувач.
Для перебору вводу від користувача використовуйте цикл. Виведіть суму цифр числа на екран.
Приклад виконання програми:
Введіть натуральне число: 12345
Сума цифр числа 12345: 15
"""
sum_of_number = 0
while True:
    number = input('Please enter any natural number ')
    if number.isdigit() and int(number) > 0:
        for i in number:
            sum_of_number += int(i)
        break
    else:
        print('PLease enter integer number > 0')
print(f'The sum of the digits of the number will be {sum_of_number}')
print()

print('task 7')
"""  Потрібно написати програму, яка просить користувача ввести числа, доки він не введе 0.
Програма повинна підрахувати суму всіх введених чисел, окрім 0, і вивести її на екран.
Це повинно працювать як калькулятор, в який ввів цифру - нажав плюс - ввів наступну цифру.
Після введеня 0 показує результат сумування.
Розв'язати з використанням циклу while та break
"""
sum_of_inputs = 0
while True:
    user_inputs = input('Please enter a number to be added to summation. To end the sum, enter 0. ')
    if not user_inputs:
        print('You didn\'t enter anything. Please enter a number.')
        continue
    try:
        user_inputs = float(user_inputs)
    except ValueError:
        print('Invalid input. Please enter a valid number.')
        continue
    if user_inputs == 0:
        break
    else:
        sum_of_inputs += user_inputs
print(f'Результат сумування: {sum_of_inputs}')
print()

print('task 8')
"""  З використанням циклу for реалізуйте гру "Вгадай число".
Початок програми написаний, гравець має 5 спроб відгадати випадкове число від 1 до 20,
яке було згенеровано за допомогою функції randint() модуля random.
У кожній спробі гравець вводить своє припущення, після чого програма повідомляє, чи
було припущення занадто великим або занадто малим, чи гравець вгадав число.
"""
import random
secret_number = random.randint(1, 20)
guesses = 0
max_guesses = 5
print("Вгадайте число від 1 до 20 за 5 спроб!")
for i in range(max_guesses):
    while True:
        try:
            selected_number = int(input('Введіть ціле число від 1 до 20 '))
            if 1 <= selected_number <= 20:
                break
            else:
                print('Число має бути від 1 до 20')
        except ValueError:
            print('Будь ласка, вводьте ціле число.')
    guesses += 1
    if selected_number == secret_number:
        print(f'Вітаю! Ви вгадали число за {guesses} сспроби')
        break
    else:
        print(f'Ви можете спробувати ще {max_guesses - guesses} разів')
else:
    print("Ви використали усі 5 спроб. Пощастить іншим разом!")
print()

print('task 9')
"""  Задача з використанням циклу for та continue. Задано список фруктів 'fruits'
потрібно вивести на екран всі елементи списку, окрім "orange".
"""
fruits = ["apple", "banana", "orange", "grape", "mango"]
excepted_fruit = 'orange'
for i in fruits:
    if  i == excepted_fruit:
        continue
    print(i)
print()

print('task 10')
"""  Задано список чисел numbers, потрібно знайти список квадратів
парних чисел зі списку. Спробуйте використати if та цикл for в один рядок.
"""
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = [i**2 for i in numbers if i % 2 == 0]
print(result)  #  [4, 16, 36, 64, 100]
print()

print('task 6.1 from LMS')
"""Порахувати кількість унікальних символів в строці. Якщо їх більше 10 - 
вивести в консоль True, інакше - False. Строку отримати за допомогою функції input()
Перевірте, що репозиторій в git є публічним або ваш вчитель доданий до цього репозиторію.
Ви можете перевірити це в інкогніто-режимі вашого браузера.
Просто вставте посилання на свій репозиторій та переконайтеся, що ви можете побачити код."""
character_count = 0
input_phrase = input('Напишіть будь-яке слово чи речення.')
for i in input_phrase:
    character_count += 1
print(character_count > 10)
print()

print('task 6.2 from LMS')
"""Напишіть цикл, який буде вимагати від користувача ввести слово, в якому є літера "h" 
(враховуються як великі так і маленькі). Цикл не повинен завершитися, якщо користувач ввів слово без букви "h".
Перевірте, що репозиторій в git є публічним або ваш вчитель доданий до цього репозиторію.
Ви можете перевірити це в інкогніто-режимі вашого браузера.
Просто вставте посилання на свій репозиторій та переконайтеся, що ви можете побачити код."""
while True:
    input_phrase = input('Write any word that contains the letter "h".')
    count = 0
    for i in input_phrase:
        if i == 'h' or i == 'H':
            count += 1
    if count >= 1:
        print(f"Thanks, for  your word '{input_phrase}'")
        break
    else:
        print("Please, enter word with the 'h' letter. ")
print()

print('task 6.3 from LMS')
"""Є list з даними lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']. 
Напишіть код, який свормує новий list (наприклад lst2), який містить лише змінні типу стрінг, які присутні в lst1. 
Данні в лісті можуть бути будь якими
Перевірте, що репозиторій в git є публічним або ваш вчитель доданий до цього репозиторію.
Ви можете перевірити це в інкогніто-режимі вашого браузера.
Просто вставте посилання на свій репозиторій та переконайтеся, що ви можете побачити код."""
lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum']
lst2 = []
for i in lst1:
    if  isinstance(i, str):
        lst2.append(i)
    else:
        continue
print(lst2)
print()

print('task 6.4 from LMS')
"""Є ліст з числами, порахуйте сумму усіх ПАРНИХ чисел в цьому лісті
Перевірте, що репозиторій в git є публічним або ваш вчитель доданий до цього репозиторію.
Ви можете перевірити це в інкогніто-режимі вашого браузера.
Просто вставте посилання на свій репозиторій та переконайтеся, що ви можете побачити код."""
random_list = []
summarized_list = 0
for i in range(20):
   random_list.append(random.randint(1, 100))
for f in random_list:
    if f % 2 == 0:
        summarized_list += f
print(f'Нам пропонується такий рандомний лист {random_list}.')
print(f'Сума парних чисел якого буде складати {summarized_list}')