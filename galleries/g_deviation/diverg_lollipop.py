import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import patches

mtcars = pd.read_csv("../data/mtcars.csv")

x = mtcars['mpg']
mtcars['mpg_z'] = (x - x.mean()) / x.std()
mtcars['colors'] = ['red' if x < 0 else 'green' for x in mtcars['mpg_z']]
mtcars.sort_values('mpg_z', inplace=True)
mtcars.reset_index(inplace=True)

_, ax = plt.subplots(dpi=100)

ax.scatter(mtcars.mpg_z,
           mtcars.index,
           color=mtcars.colors,
           s=[600 if x == 'Fiat X1-9' else 300 for x in mtcars.cars],
           alpha=0.6)

ax.barh(y=mtcars.index,
        width=mtcars.mpg_z,
        color=mtcars.colors,
        alpha=0.4,
        height=.1)

ax.annotate('Mercedes Models',
            xy=(0.0, 11.0),
            xytext=(1.0, 11),
            xycoords='data',
            fontsize='medium',
            ha='center',
            va='center',
            color='white',
            bbox=dict(boxstyle='square', fc='firebrick'),
            arrowprops=dict(arrowstyle='-[, widthB=2.0, lengthB=1.5',
                            lw=2.0,
                            color='steelblue'))

ax.set(xlabel='Mileage',
       ylabel='Model',
       yticks=mtcars.index,
       yticklabels=mtcars.cars,
       title='Diverging Bars of Car Mileage')

ax.grid(linestyle='--', alpha=0.5)
plt.show()
