
import numpy as np
from matplotlib import pyplot as plt
from collections import Counter
import pandas as pd

plt.style.use('ggplot')

data = pd.read_csv('data.csv')
ids = data['Responder_id']
print(data)
lang_responses = data['LanguagesWorkedWith']

language_counter = Counter()
for response in lang_responses:
    language_counter.update(response.split(';'))

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
