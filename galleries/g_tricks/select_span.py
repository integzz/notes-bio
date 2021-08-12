import matplotlib.pyplot as plt
from matplotlib.widgets import SpanSelector


def onselect(xmin, xmax):
    print(xmin, xmax)
    return xmin, xmax


_, ax = plt.subplots(dpi=100)

x = [1, 2, 3, 4, 5, 6, 7]
y = [10, 50, 100, 23, 15, 28, 45]

ax.plot(x, y)

span = SpanSelector(ax,
                    onselect,
                    'horizontal',
                    useblit=True,
                    rectprops=dict(alpha=0.5, facecolor='red'))
plt.show()
