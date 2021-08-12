import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

mpg = pd.read_csv("../data/mpg.csv")

g = sns.JointGrid()

sns.scatterplot(data=mpg,
                x="displ",
                y="hwy",
                hue="manufacturer",
                ax=g.ax_joint)

sns.histplot(data=mpg, x="displ", bins=40, ax=g.ax_marg_x)
sns.histplot(data=mpg, y="hwy", bins=40, ax=g.ax_marg_y)
plt.show()
