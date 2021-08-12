import matplotlib.pyplot as plt
import numpy as np

step = .1
x = np.arange(0, 10 + step, step)
y = x**2

_, ax = plt.subplots(dpi=100)
ax.plot(x, y)

axins = ax.inset_axes([0.1, 0.5, 0.4, 0.4])
axins.plot(x[:10], y[:10])

ax.indicate_inset_zoom(axins, linewidth=3)

plt.show()
