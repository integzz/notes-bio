import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mpg = pd.read_csv("../data/mpg.csv")

mpg_select = mpg.query('cyl in [4, 8]')

g = sns.lmplot(x="displ",
               y="hwy",
               hue="cyl",
               data=mpg_select,
               robust=True,
               palette='tab10',
               scatter_kws=dict(s=60, linewidths=.7, edgecolors='black'))

g.set(xlim=(0.5, 7.5),
      ylim=(0, 50),
      title="Scatterplot with line of best fit grouped by number of cylinders")
plt.show()
