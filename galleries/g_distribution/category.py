import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset("titanic")

sns.catplot(x="age",
            y="embark_town",
            hue="sex",
            col="class",
            data=titanic[titanic.embark_town.notnull()],
            orient="h",
            height=5,
            aspect=1,
            palette="tab10",
            kind="violin",
            dodge=True,
            cut=0)
plt.show()
