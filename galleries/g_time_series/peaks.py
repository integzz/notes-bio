import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
import seaborn as sns

passengers = pd.read_csv('../data/air_passengers.csv')

traffic = passengers.value
doublediff = np.diff(np.sign(np.diff(traffic)))
peak_locations = np.where(doublediff == -2)[0] + 1

doublediff2 = np.diff(np.sign(np.diff(-1 * traffic)))
trough_locations = np.where(doublediff2 == -2)[0] + 1

_, ax = plt.subplots(dpi=100)

ax.plot('date',
        'value',
        data=passengers,
        color='tab:blue',
        label='Air Traffic')

ax.scatter(passengers.date[peak_locations],
           passengers.value[peak_locations],
           marker=mpl.markers.CARETUPBASE,
           color='tab:green',
           s=100,
           label='Peaks')

ax.scatter(passengers.date[trough_locations],
           passengers.value[trough_locations],
           marker=mpl.markers.CARETDOWNBASE,
           color='tab:red',
           s=100,
           label='Troughs')

for t, p in zip(trough_locations[1::5], peak_locations[::3]):
    ax.text(passengers.date[p],
            passengers.value[p] + 15,
            passengers.date[p],
            horizontalalignment='center',
            color='darkgreen')

    ax.text(passengers.date[t],
            passengers.value[t] - 35,
            passengers.date[t],
            horizontalalignment='center',
            color='darkred')

xtick_location = passengers.index[::6]
xtick_labels = passengers.date[::6]
ytick_labels = passengers.value[::6]

sns.despine()

ax.set(ylim=(50, 750),
       yticklabels=ytick_labels,
       xticks=xtick_location,
       title='Peak and Troughs of Air Passengers Traffic (1949 - 1969)')

ax.set_xticklabels(labels=xtick_labels, rotation=90)

ax.legend(loc='upper left')
ax.grid(axis='y', alpha=.3)
plt.show()
