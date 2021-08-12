import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

from matplotlib import patches
from scipy.spatial import ConvexHull

midwest = pd.read_csv('../data/midwest_filter.csv')

_, ax = plt.subplots(dpi=150)

g = sns.scatterplot(x='area',
                    y='poptotal',
                    data=midwest,
                    hue='category',
                    palette='tab10',
                    size='dot_size',
                    ax=ax)


# Encircling
def encircle(x, y, ax=None, **kw):
    if not ax:
        ax = plt.gca()
    p = np.c_[x, y]
    hull = ConvexHull(p)
    poly = patches.Polygon(xy=p[hull.vertices, :], closed=True, **kw)
    ax.add_patch(poly)


g.set(xlim=(0.0, 0.1),
      ylim=(0, 90000),
      xlabel='Area',
      ylabel='Population',
      title='Bubble Plot with Encircling')

# Select data to be encircled
midwest_encircle_data = midwest.loc[midwest.state == 'IN', :]

# Draw polygon surrounding vertices
encircle(midwest_encircle_data.area,
         midwest_encircle_data.poptotal,
         edgecolor='k',
         facecolor='gold',
         alpha=0.1)

encircle(midwest_encircle_data.area,
         midwest_encircle_data.poptotal,
         edgecolor='firebrick',
         facecolor='none',
         linewidth=1.5)

plt.show()
