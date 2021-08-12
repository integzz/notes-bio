from yellowbrick.datasets import load_credit
from yellowbrick.features import Rank1D

X, y = load_credit()

visualizer = Rank1D(algorithm="shapiro")
visualizer.fit_transform(X)
visualizer.show()
