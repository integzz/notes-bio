import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import cell2d


class Percolation(cell2d.Cell2D):

    kernel = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])

    def __init__(self, n_rows=100, porous=0.5):
        self.n = n_rows
        self.porous = porous
        self.array = np.random.choice([1, 0], (self.n, self.n),
                                      p=[porous, 1 - porous])
        self.array[0] = 5  # fill the top row with wet cells

    def step(self):
        a = self.array
        c = correlate2d(a, self.kernel, mode='same')
        self.array[(a == 1) & (c >= 5)] = 5

    def num_wet(self):
        return np.sum(self.array == 5)

    def num_wet_bottom(self):
        return np.sum(self.array[-1] == 5)

    def draw(self):
        draw_array_2d(self.array, cmap='Blues', vmax=5)

    def test(self):
        num_wet = self.num_wet()

        while True:
            self.step()

            if self.num_wet_bottom():
                return True

            new_num_wet = self.num_wet()
            if new_num_wet == num_wet:
                return False

            num_wet = new_num_wet

    def test_fractal(self, plot=True):
        res = []
        for size in self.n:
            if self.test():
                num_filled = self.num_wet() - size
                res.append((size, size**2, num_filled))

        sizes, cells, filled = zip(*res)
        if plot:
            options = dict(linestyle='dashed', color='gray', alpha=0.7)
            ax.plot(sizes, cells, label='d=2', **options)
            ax.plot(sizes, filled, '.', label='filled')
            ax.plot(sizes, sizes, label='d=1', **options)

            ax.set(xlabel='Array Size',
                   ylabel='Cell Count',
                   xscale='log',
                   yscale='log',
                   xlim=(9, 110),
                   ylim=(9, 20000))

            ax.legend(loc='upper left')

        param_list = []
        for ys in [cells, filled, sizes]:
            params = linregress(np.log(sizes), np.log(ys))
            param_list.append(params[0])
        return param_list


def estimate_wet_fraction(n=100, porous=0.5, iters=100):
    t = [Percolation(n, porous).test() for i in range(iters)]
    return np.mean(t)


def find_critical(n=100, porous=0.6, iters=100):
    qs = [porous]
    for i in range(iters):
        if Percolation(n, porous).test():
            porous -= 0.005
        else:
            porous += 0.005
        qs.append(porous)
    return qs
