import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from matplotlib.colors import LinearSegmentedColormap
import cell2d


class ForestFire(cell2d.Cell2D):
    def __init__(self, n_rows=100, r_occupy=0.01, r_fire=0.001):
        colors = [(0, 'white'), (0.2, 'Green'), (1.0, 'Orange')]

        self.cmap = LinearSegmentedColormap.from_list('mycmap', colors)

        self.kernel = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])
        self.p = r_occupy
        self.f = r_fire
        self.n = n_rows
        self.array = np.random.choice([1, 0], (self.n, self.n),
                                      p=[self.p, 1 - self.p])

    def step(self):
        p, f = self.p, self.f
        a = self.array
        c = correlate2d(a, self.kernel, mode='same', boundary='wrap')
        r = np.random.random(a.shape)
        new_tree = (a == 0) & (r < p)
        new_fire = (a == 1) & ((c > 4) | (r < f))
        a[a == 5] = 0
        a[new_tree] = 1
        a[new_fire] = 5

    def num_trees(self, i=None):
        a = self.array[:i, :i]
        return np.sum(a == 1)

    def num_fires(self, i=None):
        a = self.array[:i, :i]
        return np.sum(a == 5)

    def draw(self):
        draw_array_2d(self.array, cmap=self.cmap, vmax=5)

    def test_fractal(self, plot=True):
        res = []
        sizes = range(10, 100)

        for i in sizes:
            res.append((i**2, self.num_trees(i), self.num_fires(i)))

        cells, trees, fires = zip(*res)

        if plot:
            options = dict(linestyle='dashed', color='gray', alpha=0.7)
            ax.plot(sizes, cells, label='cells', **options)
            ax.plot(sizes, trees, '.', label='trees', color='green')
            ax.plot(sizes, fires, label='fires', color='orange')

            ax.set(xscale='log',
                   yscale='log',
                   xlabel='Array size',
                   ylabel='Cell Count')
            ax.legend(loc='upper left')

        param_list = []
        for ys in [cells, trees]:
            params = linregress(np.log(sizes), np.log(ys))
            param_list.append(params[0])
        return param_list
