
from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

# slices = [12, 8, 3, 2]
# labels = ['60', '40', 'Extra1', 'Extra2']
# colors = ['#008fd5', '#fc4f30', '#e5ae37', '#6d904f']

# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
# i want to emphasize one on the slices
# weights point how far from the radius the slice is exploded
explode = [0, 0, 0, 0.05, 0]

plt.pie(slices, labels=labels, explode=explode, shadow=True,
        startangle=-90, autopct='%1.1f%%', wedgeprops={'edgecolor': 'black'})

plt.title('My pie chart')

plt.show()
