import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

visitors = pd.read_csv('../data/night_visitors.csv')

mycolors = [
    'tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:brown', 'tab:grey',
    'tab:pink', 'tab:olive'
]

columns = visitors.columns[1:]
labs = columns.values

x = visitors['yearmon'].values
y0 = visitors[columns[0]].values
y1 = visitors[columns[1]].values
y2 = visitors[columns[2]].values
y3 = visitors[columns[3]].values
y4 = visitors[columns[4]].values
y5 = visitors[columns[5]].values
y6 = visitors[columns[6]].values
y7 = visitors[columns[7]].values

y = np.vstack([y0, y2, y4, y6, y7, y5, y1, y3])

labs = columns.values

_, ax = plt.subplots(dpi=100)

sns.despine()

ax.stackplot(x, y, labels=labs, colors=mycolors, alpha=0.8)

ax.set(xlim=(x[0], x[-1]), title='Night Visitors in Australian Regions')
ax.legend(ncol=8)

plt.show()
