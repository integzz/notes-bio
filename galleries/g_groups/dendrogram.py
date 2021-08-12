import scipy.cluster.hierarchy as shc
import pandas as pd
import matplotlib.pyplot as plt

arrests = pd.read_csv('../data/us_arrests.csv')

_, ax = plt.subplots(dpi=100)

dend = shc.dendrogram(shc.linkage(
    arrests[['Murder', 'Assault', 'UrbanPop', 'Rape']], method='ward'),
                      labels=arrests.State.values,
                      color_threshold=100)

ax.set(title="USArrests Dendograms")
plt.show()
