import pandas as pd
import matplotlib.pyplot as plt

mtcars = pd.read_csv("../data/mtcars.csv")

x = mtcars['mpg']
mtcars['mpg_z'] = (x - x.mean()) / x.std()
mtcars['colors'] = ['red' if x < 0 else 'green' for x in mtcars['mpg_z']]
mtcars.sort_values('mpg_z', inplace=True)

_, ax = plt.subplots(figsize=(10, 6), dpi=100)

bar = ax.barh(y=mtcars.index,
              width=mtcars.mpg_z,
              color=mtcars.colors,
              alpha=0.4,
              linewidth=5)

ax.bar_label(container=bar, fmt='%0.2g', label_type='edge', padding=3)

ax.set(xlabel='Mileage',
       ylabel='Model',
       yticks=mtcars.index,
       yticklabels=mtcars.cars,
       title='Diverging Bars of Car Mileage')
ax.tick_params(axis='both', labelsize='medium')
ax.grid(linestyle='--', alpha=0.5)
plt.show()
