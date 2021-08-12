from scipy.spatial import ConvexHull
from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

arrests = pd.read_csv('../data/us_arrests.csv')

cluster = AgglomerativeClustering(n_clusters=5,
                                  affinity='euclidean',
                                  linkage='ward')
cluster.fit_predict(arrests[['Murder', 'Assault', 'UrbanPop', 'Rape']])

_, ax = plt.subplots(dpi=100)

ax.scatter(arrests.iloc[:, 0],
           arrests.iloc[:, 1],
           c=cluster.labels_,
           cmap='tab10')


def encircle(x, y, ax=None, **kw):
    if not ax:
        ax = plt.gca()
    p = np.c_[x, y]
    hull = ConvexHull(p)
    poly = plt.Polygon(p[hull.vertices, :], **kw)
    ax.add_patch(poly)


encircle(arrests.loc[cluster.labels_ == 0, 'Murder'],
         arrests.loc[cluster.labels_ == 0, 'Assault'],
         ec='k',
         fc='gold',
         alpha=0.2,
         linewidth=0)

encircle(arrests.loc[cluster.labels_ == 1, 'Murder'],
         arrests.loc[cluster.labels_ == 1, 'Assault'],
         ec='k',
         fc='tab:blue',
         alpha=0.2,
         linewidth=0)
encircle(arrests.loc[cluster.labels_ == 2, 'Murder'],
         arrests.loc[cluster.labels_ == 2, 'Assault'],
         ec='k',
         fc='tab:red',
         alpha=0.2,
         linewidth=0)

encircle(arrests.loc[cluster.labels_ == 3, 'Murder'],
         arrests.loc[cluster.labels_ == 3, 'Assault'],
         ec='k',
         fc='tab:green',
         alpha=0.2,
         linewidth=0)

encircle(arrests.loc[cluster.labels_ == 4, 'Murder'],
         arrests.loc[cluster.labels_ == 4, 'Assault'],
         ec='k',
         fc='tab:orange',
         alpha=0.2,
         linewidth=0)

ax.set(xlabel='Murder',
       ylabel='Assault',
       title='Agglomerative Clustering of USArrests (5 Groups)')
plt.show()
