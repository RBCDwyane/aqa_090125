adwentures_of_tom_sawer = """\
Tom gave up the brush with reluctance in his .... face but alacrity
in his heart. And while
the late steamer
"Big Missouri" worked ....
and sweated
in the sun,
the retired artist sat on a barrel in the .... shade close by, dangled his legs,
munched his apple, and planned the slaughter of more innocents.
There was no lack of material;
boys happened along every little while;
they came to jeer, but .... remained to whitewash. ....
By the time Ben was fagged out, Tom had traded the next chance to Billy Fisher for
a kite, in good repair;
and when he played
out, Johnny Miller bought
in for a dead rat and a string to swing it with—and so on, and so on,
hour after hour. And when the middle of the afternoon came, from being a
poor poverty, stricken boy in the .... morning, Tom was literally
rolling in wealth."""
print(adwentures_of_tom_sawer)
print()

print('task 01')
""" Дані у строці adwentures_of_tom_sawer розбиті випадковим чином, через помилку.
треба замінити кінець абзацу на пробіл .replace("\n", " ")"""
corrected_task1 = adwentures_of_tom_sawer.replace("\n", " ")
print(corrected_task1)
print()

print('task 02')
""" Замініть .... на пробіл
"""
corrected_task2 = corrected_task1.replace("....", " ")
print(corrected_task2)
print()

print('task 03')
""" Зробіть так, щоб у тексті було не більше одного пробілу між словами.
"""
corrected_task3_split = corrected_task2.split()
corrected_task3 = " ".join(corrected_task3_split)
print(corrected_task3)
print()

print('task 04')
""" Виведіть, скількі разів у тексті зустрічається літера "h"
"""
count_task4 = corrected_task3.count("h") + corrected_task3.count("H") # не впевнений, що треба було і велику шукати, але нехай буде
print(f'Літера h зустрічається {count_task4} разів у тексті')
print()

print('task 05')
""" Виведіть, скільки слів у тексті починається з Великої літери?
"""
#task5 = corrected_task3.count()
count_task5 = 0
for new_cell in corrected_task3:
    if new_cell.isupper() == True:
        count_task5 += 1
print(f'В тексті зустрічаються {count_task5} великих літер')
print()
print('task 05/2')
count_task5_2 = corrected_task3.count("A") + corrected_task3.count("B") + corrected_task3.count("C") + \
                corrected_task3.count("D") + corrected_task3.count("E") + corrected_task3.count("F") + \
                corrected_task3.count("G") + corrected_task3.count("H") + corrected_task3.count("I") + \
                corrected_task3.count("J") + corrected_task3.count("K") + corrected_task3.count("L") + \
                corrected_task3.count("M") + corrected_task3.count("N") + corrected_task3.count("O") + \
                corrected_task3.count("P") + corrected_task3.count("Q") + corrected_task3.count("R") + \
                corrected_task3.count("S") + corrected_task3.count("T") + corrected_task3.count("U") + \
                corrected_task3.count("V") + corrected_task3.count("W") + corrected_task3.count("X") + \
                corrected_task3.count("Y") + corrected_task3.count("Z") # фуух
print(f'В тексті зустрічаються {count_task5_2} великих літер')
print()

print('task 06')
""" Виведіть позицію, на якій слово Tom зустрічається вдруге
"""
second_start_position = corrected_task3.find("Tom") +1
result_task6 = corrected_task3.find("Tom", second_start_position)
print(f'Слово "Tom" зустрічається в тексті вдруге на {result_task6} позиції.')
print()

print('task 07')
""" Розділіть змінну adwentures_of_tom_sawer по кінцю речення.
Збережіть результат у змінній adwentures_of_tom_sawer_sentences
"""
adwentures_of_tom_sawer_sentences = corrected_task3.split(". ")
print(adwentures_of_tom_sawer_sentences)
print()

print('task 08')
""" Виведіть четверте речення з adwentures_of_tom_sawer_sentences.
Перетворіть рядок у нижній регістр.
"""
print(adwentures_of_tom_sawer_sentences[3].lower())
print()

print('task 09')
""" Перевірте чи починається якесь речення з "By the time".
"""
count_task9 = 0
if adwentures_of_tom_sawer_sentences[0].startswith("By the time"):
    count_task9 += 1
else:
    count_task9 += 0
if adwentures_of_tom_sawer_sentences[1].startswith("By the time"):
    count_task9 += 1
else:
    count_task9 += 0
if adwentures_of_tom_sawer_sentences[2].startswith("By the time"):
    count_task9 += 1
else:
    count_task9 += 0
if adwentures_of_tom_sawer_sentences[3].startswith("By the time"):
    count_task9 += 1
else:
    count_task9 += 0
if adwentures_of_tom_sawer_sentences[4].startswith("By the time"):
    count_task9 += 1
else:
    count_task9 += 0
print(f'В тексті знайдено {count_task9} речення з фразою "By the time" на початку')
print()

print('task 09/2')
count_task9_2 = 0
tuple_task9 = tuple(adwentures_of_tom_sawer_sentences)
for result_task9 in tuple_task9:
    if result_task9.startswith("By the time"):
        count_task9_2 += 1
    else:
        count_task9_2 += 0
print(f'В тексті знайдено {count_task9_2} речення з фразою "By the time" на початку')
print()

print('task 10')
""" Виведіть кількість слів останнього речення з adwentures_of_tom_sawer_sentences.
"""
count_words_task10 = len(adwentures_of_tom_sawer_sentences[4].split(" "))
print(f'Останнє речення містить {count_words_task10} слова.')