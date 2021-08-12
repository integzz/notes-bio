import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mtcars = pd.read_csv("../data/mtcars.csv")

_, axes = plt.subplots(figsize=(10, 6), dpi=100)
g = sns.heatmap(mtcars.corr(),
                xticklabels=mtcars.corr().columns,
                yticklabels=mtcars.corr().columns,
                cmap='RdYlGn',
                center=0,
                annot=True,
                ax=axes)

g.set(title='Correlogram of mtcars')
plt.show()
