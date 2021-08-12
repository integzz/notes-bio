import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mpg = pd.read_csv("../data/mpg.csv")

_, ax = plt.subplots(dpi=100)

g = sns.stripplot(x='cty',
                  y='hwy',
                  data=mpg,
                  jitter=0.25,
                  size=8,
                  ax=ax,
                  linewidth=.5)

g.set(title='Use jittered plots to avoid overlapping of points')
plt.show()
