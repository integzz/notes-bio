import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.colors import LinearSegmentedColormap
import cell2d


class Schelling(cell2d.Cell2D):
    options = dict(mode='same', boundary='wrap')

    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]], dtype=np.int8)

    def __init__(self, n_rows, p_frac):
        self.p = p_frac
        # 0 is empty, 1 is red, 2 is blue
        choices = np.array([0, 1, 2], dtype=np.int8)
        ps = [0.1, 0.45, 0.45]
        self.array = np.random.choice(choices, (n_rows, n_rows), p=ps)
        palette = sns.color_palette('muted')
        colors = 'white', palette[1], palette[0]
        self.cmap = LinearSegmentedColormap.from_list('cmap', colors)

    def count_neighbors(self):
        a = self.array

        empty = a == 0
        red = a == 1
        blue = a == 2

        # count red neighbors, blue neighbors, and total
        num_red = correlate2d(red, self.kernel, **self.options)
        num_blue = correlate2d(blue, self.kernel, **self.options)
        num_neighbors = num_red + num_blue

        # compute fraction of similar neighbors
        frac_red = num_red / num_neighbors
        frac_blue = num_blue / num_neighbors

        # no neighbors is considered the same as no similar neighbors
        # (this is an arbitrary choice for a rare event)
        frac_red[num_neighbors == 0] = 0
        frac_blue[num_neighbors == 0] = 0

        # for each cell, compute the fraction of neighbors with the same color
        frac_same = np.where(red, frac_red, frac_blue)

        # for empty cells, frac_same is NaN
        frac_same[empty] = np.nan

        return empty, frac_red, frac_blue, frac_same

    def segregation(self):
        _, _, _, frac_same = self.count_neighbors()
        return np.nanmean(frac_same)

    def step(self):
        a = self.array
        empty, _, _, frac_same = self.count_neighbors()

        # find the unhappy cells (ignore NaN in frac_same)
        with np.errstate(invalid='ignore'):
            unhappy = frac_same < self.p
        unhappy_locs = find_locs(unhappy)

        # find the empty cells
        empty_locs = find_locs(empty)

        # shuffle the unhappy cells
        if len(unhappy_locs):
            np.random.shuffle(unhappy_locs)

        # for each unhappy cell, choose a random destination
        num_empty = np.sum(empty)
        for source in unhappy_locs:
            i = np.random.randint(num_empty)
            dest = empty_locs[i]

            # move
            a[dest] = a[source]
            a[source] = 0
            empty_locs[i] = source

        # check that the number of empty cells is unchanged
        num_empty2 = np.sum(a == 0)
        assert num_empty == num_empty2

        # return the average fraction of similar neighbors
        return np.nanmean(frac_same)

    def draw(self):
        return draw_array_2d(self.array, cmap=self.cmap, vmax=2)


def plot_segregation(grid, ps):
    set_palette('Blues', 5, reverse=True)

    np.random.seed(17)
    for p in ps:
        segregation = [grid.step() for i in range(12)]
        ax.plot(segregation, label='p = %.1f' % p)
        print(p, segregation[-1], segregation[-1] - p)

    ax.set(xlabel='Time steps', ylabel='Segregation', ylim=(0, 1))
    ax.legend(loc='lower right')


class BigSort(Schelling):
    def __init__(self, n_rows, n_cols=None, num_compares=2):
        self.num_comps = num_compares
        super().__init__(n_rows, n_cols)

    def step(self, prob_move=0.1):
        a = self.array

        # count the neighbors
        empty, frac_red, frac_blue, frac_same = self.count_neighbors()

        # find the empty cells
        num_empty = np.sum(empty)
        empty_locs = find_locs(empty)

        # choose the cells that are moving
        r = np.random.random(a.shape)
        unhappy_locs = find_locs(~empty & (r < prob_move))

        # shuffle the unhappy cells
        if len(unhappy_locs):
            np.random.shuffle(unhappy_locs)

        # for each unhappy cell, choose a destination and move
        for source in unhappy_locs:

            # make a list of random choices
            choices = []
            indices = np.random.randint(num_empty, size=self.num_comps)
            destinations = [empty_locs[i] for i in indices]
            fracs = [frac_red[dest] for dest in destinations]
            choices = zip(fracs, indices, destinations)

            # choose a destination
            if a[source] == 1:
                # if red, maximize the fraction of red
                frac, i, dest = max(choices)
            else:
                # if blue, minimize
                frac, i, dest = min(choices)

            # move
            a[dest] = a[source]
            a[source] = 0
            empty_locs[i] = source

        # check that the number of empty cells hasn't changed
        num_empty2 = np.sum(a == 0)
        assert num_empty == num_empty2

        # return the average fraction of similar neighbors
        return np.nanmean(frac_same)


def make_locs(n_rows, n_cols):
    t = [(i, j) for i in range(n_rows) for j in range(n_cols)]
    return np.array(t)


def make_visible_array(d):
    a = np.array([[-d, 0], [d, 0], [0, -d], [0, d]])
    np.random.shuffle(a)
    return a


def make_visible_locs(vision):
    arrays = [make_visible_array(d) for d in range(1, vision + 1)]
    return np.vstack(arrays)


def compute_distances_from(size, i, j):
    X, Y = np.indices((size, size))
    return np.hypot(X - i, Y - j)


def find_locs(condition):
    return list(zip(*np.nonzero(condition)))


def set_palette(*args, **kwds):
    reverse = kwds.pop('reverse', False)
    palette = sns.color_palette(*args, **kwds)

    palette = list(palette)
    if reverse:
        palette.reverse()

    cycler = plt.cycler(color=palette)
    plt.gca().set_prop_cycle(cycler)
    return palette
