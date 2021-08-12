import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

crashes = sns.load_dataset('car_crashes')

cols = crashes.select_dtypes(include='number').columns

plt.Figure(figsize=(10, 8), dpi=100)

g = sns.FacetGrid(pd.DataFrame(cols), col=0, col_wrap=3, sharex=False)

for x, ax in g.axes_dict.items():
    sns.scatterplot(data=crashes, x=x, y='total', ax=ax)
g.tight_layout()

plt.show()
