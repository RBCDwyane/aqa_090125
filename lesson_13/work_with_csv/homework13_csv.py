"""
Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv
"""

import csv

'''with open('random.csv', newline="") as csvfile:
    reader = csv.reader((line.rstrip(',') for line in csvfile))
    header = next(reader)
    unique_random_csv = []
    for row in reader:
        if row not in unique_random_csv:
            unique_random_csv.append(row)

with open('random-michaels.csv', newline="") as csvfile:
    reader = csv.reader((line.rstrip(',') for line in csvfile))
    header = next(reader)
    unique_random_michaels_csv = []
    for row in reader:
        if row not in unique_random_michaels_csv:
            unique_random_michaels_csv.append(row)'''

def undub(filename):
    with open(filename, newline="") as csvfile:
        reader = csv.reader((line.rstrip(',') for line in csvfile))
        next(reader)
        return list({tuple(row) for row in reader})

unique_random_csv = undub('random.csv')
unique_random_michaels_csv = undub('random-michaels.csv')

for row in unique_random_michaels_csv:
    if row not in unique_random_csv:
        unique_random_csv.append(row)

with open('result_bondarenko.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(unique_random_csv)