from pandas.plotting import parallel_coordinates
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

diamonds = pd.read_csv("../data/diamonds_filter.csv")

_, ax = plt.subplots(dpi=100)

parallel_coordinates(diamonds, 'cut', colormap='Dark2')

sns.despine()

ax.set(title='Parallel Coordinated of Diamonds')
ax.grid(alpha=0.3)
plt.show()
