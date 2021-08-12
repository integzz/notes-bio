import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import correlate2d, welch
from scipy.stats import linregress
from itertools import *
import cell2d


class SandPile(cell2d.Cell2D):

    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]], dtype=np.int32)

    def __init__(self, n_rows, n_cols=None, level=9):
        n_cols = n_rows if n_cols is None else n_cols
        self.array = np.ones((n_rows, n_cols), dtype=np.int32) * level
        self.toppled_seq = []
        self.level = level

    def step(self, K=3):
        toppling = self.array > K  # K is threshold
        num_toppled = np.sum(toppling)
        self.toppled_seq.append(num_toppled)

        c = correlate2d(toppling, self.kernel, mode='same')
        self.array += c
        return num_toppled

    def drop(self):
        a = self.array
        n, m = a.shape
        index = np.random.randint(n), np.random.randint(m)
        a[index] += 1

    def run(self):
        total = 0
        for i in count(1):
            num_toppled = self.step()
            total += num_toppled
            if num_toppled == 0:
                return i, total

    def drop_and_run(self):
        self.drop()
        duration, total_toppled = self.run()
        return duration, total_toppled

    def draw(self):
        draw_array_2d(self.array, cmap='YlOrRd', vmax=5)

    def draw_four(self, levels=range(4)):
        plt.subplots(dpi=100)
        for i, level in enumerate(levels):
            plt.subplot(2, 2, i + 1)
            draw_array_2d(self.array == level, cmap='YlOrRd', vmax=1)


def count_cells_pile(array):
    n, m = array.shape
    end = min(n, m)

    res = []
    for i in range(1, end, 2):
        top = (n - i) // 2
        left = (m - i) // 2
        box = array[top:top + i, left:left + i]
        total = np.sum(box)
        res.append((i, i**2, total))

    return np.transpose(res)


def test_fractal_pile(pile, level, plot=False):
    res = count_cells_pile(pile.array == level)
    steps, steps2, cells = res

    legit = np.nonzero(cells)
    steps = steps[legit]
    steps2 = steps2[legit]
    cells = cells[legit]

    if plot:
        xlabel = 'Box Size' if level in [2, 3] else ''
        ylabel = 'Cell Count' if level in [0, 2] else ''
        options = dict(linestyle='dashed', color='gray', alpha=0.7)
        ax.plot(steps, steps2, **options)
        ax.plot(steps, cells, label='level=%d' % level)
        ax.plot(steps, steps, **options)

        ax.set(xlabel=xlabel,
               ylabel=ylabel,
               xscale='log',
               yscale='log',
               xlim=(1, 200))
        ax.legend(loc='upper left')

    params = linregress(np.log(steps), np.log(cells))
    return params[0]


def test_fractal_pile_four(pile, levels=range(4)):
    plt.subplots(dpi=100)

    dims = []
    for i, level in enumerate(levels):
        plt.subplot(2, 2, i + 1)
        dim = test_fractal_pile(pile, level, plot=True)
        dims.append(dim)

    for i, dim in enumerate(dims):
        print('%d  %0.3f' % (i, dim))


def plot_spectral_density(pile, nperseg=2048):
    pile.run()
    signal = pile.toppled_seq
    freqency, powers = welch(signal, nperseg=nperseg, fs=nperseg)
    x = nperseg
    ys = np.array([x**1.58, 1]) / 2.7e3
    ax.plot([1, x], ys, color='gray', linewidth=1)

    ax.plot(freqency, powers)
    ax.set(xlabel='Frequency',
           ylabel='Power',
           xscale='log',
           yscale='log',
           xlim=(1, 1200),
           ylim=(1e-4, 5))


def make_ss_plie(pile, height=1024):
    a = pile.array
    n, m = a.shape
    a[:, :] = 0
    a[n // 2, m // 2] = height


def run_ss_pile(n_rows, heights_power=10):
    pile = SandPile(n_rows)
    make_ss_plie(pile, 2**heights_power)
    print(pile.run())
    return pile
