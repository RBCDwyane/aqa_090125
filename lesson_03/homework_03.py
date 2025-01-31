import math
#alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n"That depends a good deal on where you want to get to," said the Cat.\n"I don't much care where ——" said Alice.\n"Then it doesn't matter which way you go," said the Cat.\n"—— so long as I get somewhere," Alice added as an explanation.\n"Oh, you're sure to do that," said the Cat, "if you only walk long enough."'
# task 01 == Розділіть змінну alice_in_wonderland так, щоб вона займала декілька фізичних лінії
# task 02 == Знайдіть та екрануйте всі символи одинарної дужки у тексті
# task 03 == Виведіть змінну alice_in_wonderland на друк
print('task 01-03')
alice_in_wonderland = '"Would you tell me, please, which way I ought to go from here?"\n' \
                      '"That depends a good deal on where you want to get to," said the Cat.\n' \
                      '"I don\'t much care where ——" said Alice.\n' \
                      '"Then it doesn\'t matter which way you go," said the Cat.\n' \
                      '"—— so long as I get somewhere," Alice added as an explanation.\n' \
                      '"Oh, you\'re sure to do that," said the Cat, "if you only walk long enough."'
print(alice_in_wonderland)
print()
"""
    # Задачі 04 -10:
    # Переведіть задачі з книги "Математика, 5 клас"
    # на мову пітон і виведіть відповідь, так, щоб було
    # зрозуміло дитині, що навчається в п'ятому класі
"""

print('task 04')
"""
Площа Чорного моря становить 436 402 км2, а площа Азовського
моря становить 37 800 км2. Яку площу займають Чорне та Азов-
ське моря разом?
"""
black_sea = 436402
azov_sea = 37800
total_sea_area = black_sea + azov_sea
print(f"Загальна площа Чорного та Азовського морів розраховується через суму їх площ і дорівнює {total_sea_area}км2")
print()

print('task 05')
"""
Мережа супермаркетів має 3 склади, де всього розміщено
375 291 товар. На першому та другому складах перебуває
250 449 товарів. На другому та третьому – 222 950 товарів.
Знайдіть кількість товарів, що розміщені на кожному складі.
"""
sum_of_first_second = 250449
sum_of_second_third = 222950
total_items_on_warehouses = 375291
first_warehouse = total_items_on_warehouses - sum_of_second_third
third_warehouse = total_items_on_warehouses - sum_of_first_second
second_warehouse = total_items_on_warehouses - first_warehouse - third_warehouse
print(f'Використовуючи надані дані, віднявши суму товарів на 2му та 3му складі від загальної кількості,'
      f' ми отримаємо кількість товарів на 1му складі - {first_warehouse} шт')
print(f'Далі віднявши суму товарів на 1му та 2му складі від загальної кількості,'
      f' ми отримаємо кількість товарів на 3му складі - {third_warehouse} шт')
print(f'Та підсумовуючи, віднявши, отримані кількості, на 1му та 3му складі від загальної кількості, '
      f'ми отримаємо кількість товарів на 2му складі - {second_warehouse} шт')
print()

print('task 06')
"""
Михайло разом з батьками вирішили купити комп’ютер, ско-
риставшись послугою «Оплата частинами». Відомо, що сплачу-
вати необхідно буде півтора року по 1179 грн/місяць. Обчисліть
вартість комп’ютера.
"""
credit_period = 18
monthly_payment = 1179
computer_price = credit_period * monthly_payment
print('Для того, щоб дізнатися повну вартість компьютера - треба помножити місячний платіж на кількість '
      f'місяців умовлених росстрочкою. Тож повна вартість компьютера - {computer_price} грн')
print()

print('task 07')
"""
Знайди остачу від діленя чисел:
a) 8019 : 8     d) 7248 : 6
b) 9907 : 9     e) 7128 : 5
c) 2789 : 5     f) 19224 : 9
"""
task_a = 8019 % 8
task_b = 9907 % 9
task_c = 2789 % 5
task_d = 7248 % 6
task_e = 7128 % 5
task_f = 19224 % 9
print('Нижче приведені остачі від діленя по таким числам:')
print(f'для (8019 : 8) буде {task_a}      для (7248 : 6) буде {task_d}\n'
      f'для (9907 : 9) буде {task_b}      для (7128 : 5) буде {task_e}\n'
      f'для (2789 : 5) буде {task_c}      для (19224: 9) буде {task_f}')
print()

print('task 08')
"""
Іринка, готуючись до свого дня народження, склала список того,
що їй потрібно замовити. Обчисліть, скільки грошей знадобиться
для даного її замовлення.
Назва товару    Кількість   Ціна
Піца велика     4           274 грн
Піца середня    2           218 грн
Сік             4           35 грн
Торт            1           350 грн
Вода            3           21 грн
"""
pizza_xl = 274
pizza_m = 218
juice = 35
cake = 350
water = 21
total_bill = 4*pizza_xl + 2*pizza_m + 4*juice + cake + 3*water
print('Щоб дізнатися скільки Іринка витратить на всі продукти, треба перемножити ціна них на їх вартість:\n'
      f'Піца велика, 4шт = {pizza_xl}грн\n'
      f'Піца середня, 2шт = {pizza_m}грн\n'
      f'Сік, 4шт = {juice}грн\n'
      f'Торт, 1шт = {cake}грн\n'
      f'Вода, 3шт = {water}грн')
print(f'Тоді повна сума до сплати буде - {total_bill}грн')
print()


print('task 09')
"""
Ігор займається фотографією. Він вирішив зібрати всі свої 232
фотографії та вклеїти в альбом. На одній сторінці може бути
розміщено щонайбільше 8 фото. Скільки сторінок знадобиться
Ігорю, щоб вклеїти всі фото?
"""
photos_quantity = 232
placed_quantity_on_page = 8
total_pages = photos_quantity / placed_quantity_on_page
total_sheet = total_pages / 2
print(f'Для того, щоб Ігор міг розмістити свої 232 фотографії на сторінках, на які можна розмістити тільки '
      f'по 8 фото,\nйому знадобляться {int(total_pages)} сторінок чи {math.ceil(total_sheet)} повних аркушів.')
print()

print('task 10')
"""
Родина зібралася в автомобільну подорож із Харкова в Буда-
пешт. Відстань між цими містами становить 1600 км. Відомо,
що на кожні 100 км необхідно 9 літрів бензину. Місткість баку
становить 48 літрів.
1) Скільки літрів бензину знадобиться для такої подорожі?
2) Скільки щонайменше разів родині необхідно заїхати на зап-
равку під час цієї подорожі, кожного разу заправляючи пов-
ний бак?
"""
travel_distance = 1600
gas_consumption = 9
tank_volume = 48
gas_amount_for_trip = travel_distance / 100 * 9
count_of_refills = gas_amount_for_trip / tank_volume
print('Щоб дізнатися кількість літрів, потребуємого для цьої подорожі, треба поділити відстань на 100км, '
      f'щоб дізнавшись \nкількість таких ділянок, помножити їх на відому нам витрату палива на 100км. '
      f'Ця кількість буде дорівнювати {int(gas_amount_for_trip)} літра.')
print('Знаучи кількість бензина, яка потрібна нам на подорож, то розділивши її на обʼєм баку авто, з невеликою '
      f'похибкою, \nзаправку треба буде виконоти не меньше ніж {int(count_of_refills)} рази за подорож при умові, '
      'що подорож починається з повного баку.')