import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

passengers = pd.read_csv('../data/air_passengers.csv')
date = passengers['date'].astype('datetime64')

passengers['year'] = [datetime.strftime(d, '%Y') for d in date]
passengers['month'] = [datetime.strftime(d, '%b') for d in date]
years = passengers['year'].unique()

mycolors = [
    'tab:red', 'tab:blue', 'tab:green', 'tab:orange', 'tab:brown', 'tab:grey',
    'tab:pink', 'tab:olive', 'deeppink', 'steelblue', 'firebrick',
    'mediumseagreen'
]

_, ax = plt.subplots(dpi=100)

for i, y in enumerate(years):
    ax.plot('month',
            'value',
            data=passengers.loc[passengers['year'] == y, :],
            color=mycolors[i],
            label=y)
    ax.text(passengers.loc[passengers['year'] == y, :].shape[0] - .9,
            passengers.loc[passengers['year'] == y, 'value'][-1:].values[0],
            y,
            fontsize='small',
            color=mycolors[i])

ax.set(xlim=(-0.3, 11),
       ylim=(50, 750),
       ylabel='Air Traffic',
       title="Monthly Seasonal Plot: Air Passengers Traffic (1949 - 1969)")
ax.grid(axis='y', alpha=.3)
plt.show()
