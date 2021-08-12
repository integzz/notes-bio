import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import sem
import seaborn as sns

orders = pd.read_csv('../data/user_orders_hourofday.csv')
orders_mean = orders.groupby('order_hour_of_day').quantity.mean()
orders_se = orders.groupby('order_hour_of_day').quantity.apply(sem).mul(1.96)

x = orders_mean.index

_, ax = plt.subplots(dpi=100)

sns.despine()

s, e = ax.get_xlim()

ax.set(xlim=(s, e),
       xlabel='Hour of Day',
       ylabel='# Orders',
       title='User Orders by Hour of Day (95% confidence)')
ax.plot(x, orders_mean, color='white', lw=2)
ax.fill_between(x,
                orders_mean - orders_se,
                orders_mean + orders_se,
                color='#3F5D7D')

for y in range(8, 20, 2):
    ax.hlines(y,
              xmin=s,
              xmax=e,
              colors='black',
              alpha=0.5,
              linestyles='--',
              lw=0.5)

plt.show()
