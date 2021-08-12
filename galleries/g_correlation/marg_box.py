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

sns.boxplot(data=mpg, x="displ", ax=g.ax_marg_x)
sns.boxplot(data=mpg, y="hwy", ax=g.ax_marg_y)
plt.show()
