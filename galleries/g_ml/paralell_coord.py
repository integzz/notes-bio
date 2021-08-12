from sklearn.datasets import load_wine
from yellowbrick.features import parallel_coordinates
import matplotlib.pyplot as plt

_, ax = plt.subplots(dpi=100)

X, y = load_wine(return_X_y=True)
visualizer = parallel_coordinates(X, y, normalize="standard")
