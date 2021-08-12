from joypy import joyplot
from matplotlib import pyplot as plt
import seaborn as sns

iris = sns.load_dataset('iris')

joyplot(iris, by="species", ylim='own')
# joyplot(iris, by="species", ylim='max')
# joyplot(iris, by="species", overlap=3)

plt.show()
