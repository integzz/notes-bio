import matplotlib.pyplot as plt

_, ax = plt.subplots(figsize=(10, 8), dpi=100)

x1 = [(5, 5), (20, 5), (20, 7)]
y1 = (2, 1)
ax.broken_barh(x1, y1, facecolors='green')

x2 = [(6, 2), (17, 5), (50, 2)]
y2 = (15, 1)
ax.broken_barh(x2, y2, facecolors='orange')

x3 = [(5, 2), (28, 5), (40, 2)]
y3 = (30, 1)
ax.broken_barh(x3, y3, facecolors='red')

ax.set(xlabel='Sales', ylabel='Days of the Month')
plt.show()
