import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

mpg = pd.read_csv('../data/mpg.csv')
mpg['_class'] = mpg['class']
x_var, group_var = 'displ', 'class'
mpg_agg = mpg[[x_var, group_var]].groupby(group_var)

_, ax = plt.subplots(dpi=100)

sns.histplot(data=mpg,
             x=x_var,
             hue=group_var,
             bins=30,
             multiple="stack",
             ax=ax)

ax.set(ylim=(0, 25),
       xlabel=x_var,
       ylabel='Frequency',
       title=f'Stacked Histogram of ${x_var}$ colored by ${group_var}$')
plt.show()
