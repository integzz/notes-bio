import numpy as np
import matplotlib.pyplot as plt
import cell2d


class DiffusionSelf(cell2d.Cell2D):
    kernel = np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]])

    def __init__(self, n_rows, r_dfs=0.1):
        self.r_dfs = r_dfs  # 扩散常数
        self.array = np.zeros((n_rows, n_rows), np.float)

    def add_cells(self, row, col, *strings):
        for i, s in enumerate(strings):
            self.array[row + i,
                       col:col + len(s)] = np.array([int(b) for b in s])

    def step(self):
        c = correlate2d(self.array, self.kernel, mode='same')
        self.array += self.r_dfs * c  # 关联了浓度差与流速

    def draw(self):
        draw_array_2d(self.array, cmap='Reds')


class DiffusionReaction(DiffusionSelf):

    kernel = np.array([[.05, .2, .05], [.2, -1, .2], [.05, .2, .05]])

    def __init__(self, n, params, noise=0.1):

        self.params = params
        self.array1 = np.ones((n, n), dtype=float)
        self.array2 = noise * np.random.random((n, n))
        make_island(self.array2)

    def step(self):
        A = self.array1
        B = self.array2
        ra, rb, f, k = self.params

        options = dict(mode='same', boundary='wrap')

        cA = correlate2d(A, self.kernel, **options)
        cB = correlate2d(B, self.kernel, **options)
        reaction = A * B**2
        self.array1 += ra * cA - reaction + f * (1 - A)
        self.array2 += rb * cB + reaction - (f + k) * B

    def loop100(self):
        self.loop(100)

    def draw(self):
        options = dict(interpolation='bicubic', vmin=None, vmax=None)
        draw_array_2d(self.array1, cmap='Reds', **options)
        draw_array_2d(self.array2, cmap='Blues', **options)


def make_island(a, height=0.1):
    n, m = a.shape
    radius = min(n, m) // 20
    i = n // 2
    j = m // 2
    a[i - radius:i + radius, j - radius:j + radius] += height


def draw_diffusion(f, k):
    params = 0.5, 0.25, f, k
    rd = DiffusionReaction(100, params)
    draw_three(rd, [1000, 2000, 4000])


def draw_three(grid, n_seq, seed=17):
    np.random.seed(seed)
    plt.subplots()

    for i, n in enumerate(n_seq):
        plt.subplot(1, 3, i + 1)
        grid.loop(n)
        grid.draw()
