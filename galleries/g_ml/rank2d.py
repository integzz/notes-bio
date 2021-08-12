from yellowbrick.datasets import load_bikeshare
from yellowbrick.features import Rank2D
import matplotlib.pyplot as plt

X, y = load_bikeshare()

_, ax = plt.subplots(dpi=100)

visualizer = Rank2D(algorithm="pearson")
visualizer.fit_transform(X)
visualizer.show()
