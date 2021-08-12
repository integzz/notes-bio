import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

gdp = pd.read_csv('../data/gdp_per_cap.csv')

gdp_new = gdp.melt(id_vars=['continent'],
                   value_vars=['1952', '1957'],
                   var_name='time',
                   value_name='total',
                   ignore_index=False)

_, ax = plt.subplots(dpi=100)

sns.pointplot(data=gdp_new,
              x='time',
              y='total',
              hue='continent',
              ci="sd",
              ax=ax)

sns.despine()

ax.vlines(x=0,
          ymin=gdp_new['total'].min(),
          ymax=gdp_new['total'].max(),
          colors='k',
          linestyle='dotted')
ax.vlines(x=1,
          ymin=gdp_new['total'].min(),
          ymax=gdp_new['total'].max(),
          colors='k',
          linestyle='dotted')

ax.set(xlabel='Time',
       ylabel='Mean GDP Per Capita',
       title='Slopechart: Comparing GDP Per Capita between 1952 vs 1957\n')

ax.legend(loc='center',
          bbox_to_anchor=(0.5, 1),
          ncol=len(gdp_new['continent'].unique()),
          fontsize='x-small')
plt.show()
