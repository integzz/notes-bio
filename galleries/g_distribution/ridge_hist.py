from joypy import joyplot
from matplotlib import pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')

joyplot(iris,
        by="species",
        column=["sepal_width", "petal_length"],
        hist=True,
        bins=20,
        overlap=0,
        grid=True,
        legend=False)

plt.show()
