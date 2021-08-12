import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patches

mpg = pd.read_csv('../data/mpg.csv')
mpg_group = mpg[['cty', 'manufacturer'
                 ]].groupby('manufacturer').apply(lambda x: x.mean())
mpg_group.sort_values('cty', inplace=True)
mpg_group.reset_index(inplace=True)

fig, ax = plt.subplots(facecolor='white', dpi=100)

ax.bar(x=mpg_group.index, height=mpg_group.cty)

for i, cty in enumerate(mpg_group.cty):
    ax.text(i, cty + 0.5, round(cty, 1), horizontalalignment='center')

p1 = patches.Rectangle((.57, -0.005),
                       width=.33,
                       height=.13,
                       alpha=.1,
                       facecolor='green',
                       transform=fig.transFigure)
p2 = patches.Rectangle((.124, -0.005),
                       width=.446,
                       height=.13,
                       alpha=.1,
                       facecolor='red',
                       transform=fig.transFigure)
fig.add_artist(p1)
fig.add_artist(p2)

ax.set(ylim=(0, 30),
       ylabel='Miles Per Gallon',
       xticks=mpg_group.index,
       title='Bar Chart for Highway Mileage')

ax.set_xticklabels(mpg_group.manufacturer.str.upper(),
                   rotation=60,
                   horizontalalignment='right')
plt.show()
