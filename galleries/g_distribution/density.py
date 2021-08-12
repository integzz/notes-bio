import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mpg = pd.read_csv('../data/mpg.csv')
mpg['_class'] = mpg['class']

_, ax = plt.subplots(dpi=100)

sns.histplot(data=mpg.query("_class == 'compact'"),
             x='cty',
             color="dodgerblue",
             label="Compact",
             stat='density',
             alpha=.5,
             kde=True,
             ax=ax)

sns.histplot(data=mpg.query("_class == 'suv'"),
             x="cty",
             color="orange",
             label="SUV",
             stat='density',
             alpha=.5,
             kde=True)

sns.histplot(data=mpg.query("_class == 'minivan'"),
             x="cty",
             color="g",
             label="minivan",
             stat='density',
             alpha=.5,
             kde=True)

ax.set(title='Density Plot of City Mileage by Vehicle Type')
ax.legend()
plt.show()
