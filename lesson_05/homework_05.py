small_list = [3, 1, 4, 5, 2, 5, 3]
big_list = [3, 5, -2, -1, -3, 0, 1, 4, 5, 2]
print("task 1")
# Знайдіть всі унікальні елементи в списку small_list
unique_small_list = set(small_list)
task1_small_list = list(unique_small_list)
print(task1_small_list)
print()

print("task 2")
# Знайдіть середнє арифметичне всіх елементів у списку small_list
sum_small_list = sum(small_list)
lenght_small_list = len(small_list)
avg_small_list = sum_small_list / lenght_small_list
print(f'середнє арифметичне списку є {avg_small_list}')
print()

print("task 3")
# Перевірте, чи є в списку big_list дублікати
unique_big_list = set(big_list)
duplicates_big_list = len(big_list) - len(unique_big_list)
print(f'у списку знаходиться {duplicates_big_list} дублікат')
print()

base_dict = {'contry':'Ukraine', 'continent': 'Europe', 'size': 123}
add_dict = {"a":1, "b":2, "c":2, "d":3, 'size': 12}
print('task 4')
# Знайдіть ключ з максимальним значенням у словнику add_dict
max_key = max(add_dict, key=add_dict.get)
print(f'ключ з максимальним значенням у словнику це {max_key}')
print()

print('task 5')
# Створіть новий словник, в якому ключі та значення будуть
# замінені місцями у заданому словнику
keys_list = list(base_dict.keys())
values_list = list(base_dict.values())
reversed_dictionary = dict(zip(keys_list, values_list[::-1]))
print(reversed_dictionary)
print()

print('task 6')
# Об'єднайте два словника base_dict та add_dict  в новий словник sum_dict
# Якщо ключі збігаються, то перетворіть значення в строку та об'єднайте їх
get_keys = base_dict.keys() | add_dict.keys()
def merged_duplikats(key):
    if key in base_dict and key in add_dict:
        return str(base_dict[key]) + str(add_dict[key])
    return base_dict.get(key, add_dict.get(key))
sum_dict = {key:merged_duplikats(key) for key in get_keys}
print(sum_dict)
print()

print('task 7')
line = "Створіть множину всіх символів, які входять у заданий рядок"
new_set = set(line)
print(f'за умови, що Пайтон вважає пробіл символом, то множина буде мати таке наповнення:\n{new_set}')
print()

print('task 8')
# Обчисліть суму елементів двох множин, які не є спільними
set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 6, 5, 10}
final_sum_set = sum(set_1 ^ set_2)
print(f'сума елементів двох множин буде дорівнювати {final_sum_set}')
print()

print('task 9')
# Створіть два списки та обробіть їх так, щоб отримати сет, який
# містить всі елементи з обох списків,  які зустрічаються тільки один раз.
# Наприклад, якщо перший список містить [1, 2, 3, 4], а другий
# список містить [3, 4, 5, 6], то повернутий сет містить [1, 2, 5, 6]
first_list = [12, 23, 34, 45, 2 , 4, 6, 78]
second_list = [34, 90, 6, 45, 78, 5, 8, 44]
final_set = set(first_list) ^ set(second_list)
print(final_set)
print()

print('task 10')
# Обробіть список кортежів person_list, що містять ім'я та вік людей,
# так, щоб отримати словник, де ключі - вікові діапазони (10-19, 20-29 тощо),
# а значення - списки імен людей, які потрапляють в кожен діапазон.
# Приклад виводу:
# {'10-19': ['A'], '20-29': ['B', 'C', 'D'], '30-39': ['E'], '40-49': ['F']}
person_list = [('Alice', 25), ('Boby', 19), ('Charlie', 32),
               ('David', 28), ('Emma', 22), ('Frank', 45)]
new_dict = dict(person_list)
new_list = []
for name, age in new_dict.items():
    if 10 <= age <=19:
        new_list.append(('10-19', name))
    elif 20 <= age <=29:
        new_list.append(('20-29', name))
    elif 30 <= age <=39:
        new_list.append(('30-39', name))
    elif 40 <= age <=49:
        new_list.append(('40-49', name))
    else:
        continue
final_dict = {}
for age, name in new_list:
    final_dict.setdefault(age, []).append(name)
print(final_dict)
print()

print('Task 5.1 from LMS')
# Існує деяка інформація про автомобілі з кольором, роком випуску, об'ємом двигуна, типом автомобіля та ціною.
# Маємо критерії пошуку у вигляді кортежу (рік ≥, об'єм двигуна ≥, ціна ≤). Напишіть код, який допоможе нам отримати
# автомобілі, які відповідають критеріям пошуку. Автомобілі повинні бути відсортовані за зростанням ціни. Ми повинні
# вивести до п'яти (5) перших знайдених елементів
car_data = {
  'Mercedes': ('silver', 2019, 1.8, 'sedan', 50000),
  'Audi': ('black', 2020, 2.0, 'sedan', 55000),
  'BMW': ('white', 2018, 3.0, 'suv', 70000),
  'Lexus': ('gray', 2016, 2.5, 'coupe', 45000),
  'Toyota': ('blue', 2021, 1.6, 'hatchback', 25000),
  'Honda': ('red', 2017, 1.5, 'sedan', 30000),
  'Ford': ('green', 2019, 2.3, 'suv', 40000),
  'Chevrolet': ('purple', 2020, 1.4, 'hatchback', 22000),
  'Nissan': ('pink', 2018, 1.8, 'sedan', 35000),
  'Volkswagen': ('brown', 2021, 1.4, 'hatchback', 28000),
  'Hyundai': ('gray', 2019, 1.6, 'suv', 32000),
  'Kia': ('white', 2020, 2.0, 'sedan', 28000),
  'Volvo': ('silver', 2017, 1.8, 'suv', 45000),
  'Subaru': ('blue', 2018, 2.5, 'wagon', 35000),
  'Mazda': ('red', 2019, 2.5, 'sedan', 32000),
  'Porsche': ('black', 2017, 3.0, 'coupe', 80000),
  'Jeep': ('green', 2021, 3.0, 'suv', 50000),
  'Chrysler': ('gray', 2016, 2.4, 'sedan', 22000),
  'Dodge': ('yellow', 2020, 3.6, 'suv', 40000),
  'Ferrari': ('red', 2019, 4.0, 'coupe', 500000),
  'Lamborghini': ('orange', 2021, 5.0, 'coupe', 800000),
  'Maserati': ('blue', 2018, 4.7, 'coupe', 100000),
  'Bugatti': ('black', 2020, 8.0, 'coupe', 2000000),
  'McLaren': ('yellow', 2017, 4.0, 'coupe', 700000),
  'Rolls-Royce': ('white', 2019, 6.8, 'sedan', 500000),
  'Bentley': ('gray', 2020, 4.0, 'coupe', 300000),
  'Jaguar': ('red', 2016, 2.0, 'suv', 40000),
  'Land Rover': ('green', 2018, 3.0, 'suv', 60000),
  'Tesla': ('silver', 2020, 0.0, 'sedan', 60000),
  'Acura': ('white', 2017, 2.4, 'suv', 40000),
  'Cadillac': ('black', 2019, 3.6, 'suv', 55000),
  'Infiniti': ('gray', 2018, 2.0, 'sedan', 35000),
  'Lincoln': ('white', 2021, 2.0, 'suv', 50000),
  'GMC': ('blue', 2016, 1.5, 'pickup', 30000),
  'Ram': ('black', 2019, 5.7, 'pickup', 40000),
  'Chevy': ('red', 2017, 2.4, 'pickup', 35000),
  'Dodge Ram': ('white', 2020, 3.6, 'pickup', 45000),
  'Ford F-Series': ('gray', 2021, 3.5, 'pickup', 50000),
  'Nissan Titan': ('silver', 2018, 5.6, 'pickup', 35000)
}
search_criteria = (2017, 1.6, 36000)
filtered_dict = {}
for name, data in car_data.items():
    if data[1] >= search_criteria[0] and data[2] >= search_criteria[1] and data[4] <= search_criteria[2]:
        filtered_dict[name] = data
sorted_dict = sorted(filtered_dict.items(), key=lambda x: x[1][4])
final_fs_dict = dict(sorted_dict[:5])
print(sorted_dict)
print()

print('Task 5.2 from LMS')
# Given list of tuples (name, surname, age, profession, City location)
# 1 - Add your new record o the beginning of the given list
# 2 - In modified list swap elements with indexes 1 and 5 (1<->5). Print result
# 3 - check that all people in modified list with records indexes 6, 10, 13
#   have age >=30. Print condition check result

people_records = [
  ('John', 'Doe', 28, 'Engineer', 'New York'),
  ('Alice', 'Smith', 35, 'Teacher', 'Los Angeles'),
  ('Bob', 'Johnson', 45, 'Doctor', 'Chicago'),
  ('Emily', 'Williams', 30, 'Artist', 'San Francisco'),
  ('Michael', 'Brown', 22, 'Student', 'Seattle'),
  ('Sophia', 'Davis', 40, 'Lawyer', 'Boston'),
  ('David', 'Miller', 33, 'Software Developer', 'Austin'),
  ('Olivia', 'Wilson', 27, 'Marketing Specialist', 'Denver'),
  ('Daniel', 'Taylor', 38, 'Architect', 'Portland'),
  ('Grace', 'Moore', 25, 'Graphic Designer', 'Miami'),
  ('Samuel', 'Jones', 50, 'Business Consultant', 'Atlanta'),
  ('Emma', 'Hall', 31, 'Chef', 'Dallas'),
  ('William', 'Clark', 29, 'Financial Analyst', 'Houston'),
  ('Ava', 'White', 42, 'Journalist', 'San Diego'),
  ('Ethan', 'Anderson', 36, 'Product Manager', 'Phoenix')
]
people_records.insert(0, ('Kostiantyn', 'Bondarenko', 33, 'Engineer', 'Kharkiv'))

swapped_list = []
for index in people_records:
    swapped_list.append((index[4], index[1], index[2], index[3], index[0]))
print(swapped_list)

filtered_older_list = []
for i in (6, 10, 13):
    if swapped_list[i][2] >= 30:
        filtered_older_list.append(swapped_list[i])
print(filtered_older_list)
