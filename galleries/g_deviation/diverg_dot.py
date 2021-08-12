import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mtcars = pd.read_csv("../data/mtcars.csv")

x = mtcars['mpg']
mtcars['mpg_z'] = (x - x.mean()) / x.std()
mtcars['colors'] = ['red' if x < 0 else 'green' for x in mtcars['mpg_z']]
mtcars.sort_values('mpg_z', inplace=True)
mtcars.reset_index(inplace=True)

_, ax = plt.subplots(dpi=100)

ax.scatter(mtcars.mpg_z, mtcars.index, s=450, alpha=.6, color=mtcars.colors)

for x, y, tex in zip(mtcars.mpg_z, mtcars.index, mtcars.mpg_z):
    ax.text(x,
            y,
            round(tex, 1),
            horizontalalignment='center',
            verticalalignment='center',
            fontdict={'color': 'white'})

sns.despine()

ax.set(xlabel='Mileage',
       ylabel='Model',
       yticks=mtcars.index,
       yticklabels=mtcars.cars,
       title='Diverging Dotplot of Car Mileage')

ax.grid(linestyle='--', alpha=0.5)
plt.show()
