import pandas as pd
import matplotlib.pyplot as plt

mpg = pd.read_csv('../data/mpg.csv')
mpg_group = mpg[['cty', 'manufacturer'
                 ]].groupby('manufacturer').apply(lambda x: x.mean())
mpg_group.sort_values('cty', inplace=True)
mpg_group.reset_index(inplace=True)

_, ax = plt.subplots(dpi=100)

markerline, stemlines, _ = ax.stem(mpg_group.index, mpg_group.cty)
stemlines.set_color('firebrick')
markerline.set_markerfacecolor('firebrick')
markerline.set_markeredgecolor('firebrick')

ax.set(ylim=(0, 30),
       ylabel='Miles Per Gallon',
       xticks=mpg_group.index,
       title='Lollipop Chart for Highway Mileage')

ax.set_xticklabels(mpg_group.manufacturer.str.upper(),
                   rotation=60,
                   horizontalalignment='right')

for row in mpg_group.itertuples():
    ax.text(row.Index,
            row.cty + .5,
            s=round(row.cty, 2),
            horizontalalignment='center',
            verticalalignment='bottom',
            fontsize='small')

plt.show()
