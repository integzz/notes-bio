import statsmodels.tsa.stattools as stattools
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

mortality = pd.read_csv('../data/mortality.csv')

x, y = mortality['mdeaths'], mortality['fdeaths']

ccs = stattools.ccf(x, y)[:100]
nlags = len(ccs)

conf_level = 2 / np.sqrt(nlags)

_, ax = plt.subplots(dpi=100)

ax.hlines(0, xmin=0, xmax=100, color='gray')
ax.hlines(conf_level, xmin=0, xmax=100, color='gray')
ax.hlines(-conf_level, xmin=0, xmax=100, color='gray')

ax.bar(x=np.arange(len(ccs)), height=ccs, width=.3)

ax.set(xlim=(0, len(ccs)),
       title='$Cross\ Correlation\ Plot:\ mdeaths\ vs\ fdeaths$')
plt.show()
