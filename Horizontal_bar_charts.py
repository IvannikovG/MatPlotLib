import csv
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter

plt.style.use('ggplot')

with open('data.csv') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    language_counter = Counter()
    row = next(csv_reader)

    for row in csv_reader:
        language_counter.update(row['LanguagesWorkedWith'].split(';'))
    # print(row)

languages = []
popularity = []

for item in language_counter.most_common(15):
    languages.append(item[0])
    popularity.append(item[1])

print(languages)
print(popularity)

languages.reverse()
popularity.reverse()

plt.barh(languages, popularity)

plt.title('Most popular languages')
plt.xlabel('Number of people using')
plt.grid(True)

plt.show()
