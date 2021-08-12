from yellowbrick.datasets import load_bikeshare
from yellowbrick.regressor import ResidualsPlot
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Create training and test sets
X, y = load_bikeshare()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)

visualizer = ResidualsPlot(LinearRegression())
visualizer.fit(X_train, y_train)
visualizer.score(X_test, y_test)
visualizer.show()
