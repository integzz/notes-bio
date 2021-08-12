import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

economics = pd.read_csv('../data/economics.csv')

x = economics['date']
y1 = economics['psavert']
y2 = economics['unemploy']

_, ax = plt.subplots(dpi=100)
ax.plot(x, y1, color='tab:red')

# Plot Line2 (Right Y Axis)
ax2 = ax.twinx()  # instantiate a second axes that shares the same x-axis
ax2.plot(x, y2, color='tab:blue')

ax.set(xlabel='Year', ylabel='Personal Savings Rate')
ax.tick_params(axis='x', rotation=0)
ax.tick_params(axis='y', rotation=0, labelcolor='tab:red')
ax.grid(alpha=.4)

ax2.tick_params(axis='y', labelcolor='tab:blue')
ax2.set(
    ylabel='# Unemployed (1000\'s)',
    title='Personal Savings Rate vs Unemployed: Plotting in Secondary Y Axis')
plt.show()
