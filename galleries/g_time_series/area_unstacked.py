import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

economics = pd.read_csv('../data/economics.csv')

x = economics['date'].values
y1 = economics['psavert'].values
y2 = economics['uempmed'].values

mycolors = [
    'tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:brown', 'tab:grey',
    'tab:pink', 'tab:olive'
]
columns = ['psavert', 'uempmed']

_, ax = plt.subplots(dpi=100)

ax.fill_between(x,
                y1=y1,
                y2=0,
                label=columns[1],
                alpha=0.5,
                color=mycolors[1],
                linewidth=2)
ax.fill_between(x,
                y1=y2,
                y2=0,
                label=columns[0],
                alpha=0.5,
                color=mycolors[0],
                linewidth=2)

sns.despine()

ax.set(title='Personal Savings Rate vs Median Duration of Unemployment')
ax.legend(loc='best')

plt.show()
