from yellowbrick.datasets import load_occupancy
from yellowbrick.features import RadViz

X, y = load_occupancy()

visualizer = RadViz(classes=["unoccupied", "occupied"])

visualizer.fit(X, y)
visualizer.transform(X)
visualizer.show()
