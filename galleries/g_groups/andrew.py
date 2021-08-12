from pandas.plotting import andrews_curves
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

mtcars = pd.read_csv("../data/mtcars.csv")
mtcars.drop(['cars', 'carname'], axis=1, inplace=True)

_, ax = plt.subplots(dpi=100)

andrews_curves(mtcars, 'cyl', colormap='Set1')

sns.despine()

ax.set(xlim=(-3, 3), title='Andrews Curves of mtcars')
ax.grid(alpha=0.3)
plt.show()
