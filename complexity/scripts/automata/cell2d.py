import numpy as np
import matplotlib.pyplot as plt
from IPython.display import clear_output
from time import sleep


class Cell2D:
    def __init__(self, n_rows, n_cols=None, mode=None):
        n_cols = n_rows if n_cols is None else n_cols
        self.array = np.zeros((n_rows, n_cols), np.uint8)
        if mode == 'gol':
            self.kernel = np.array([[1, 1, 1], [1, 10, 1], [1, 1, 1]])
            self.table = np.zeros(20, dtype=np.uint8)
            self.table[[3, 12, 13]] = 1
        if mode == 'high':
            self.table = np.zeros(20, dtype=np.uint8)
            self.table[[3, 12, 13]] = 1

    def add_cells(self, row, col, *strings):
        for i, s in enumerate(strings):
            self.array[row + i,
                       col:col + len(s)] = np.array([int(b) for b in s])

    def step(self):
        c = correlate2d(self.array, self.kernel, mode='same')
        self.array = self.table[c]

    def loop(self, iters=1):
        for _ in range(iters):
            self.step()

    def draw(self, cmap='Blues', **options):
        draw_array_2d(self.array)

    def animate(self, frames, interval=None, step=None):
        if step is None:
            step = self.step

        plt.subplots()
        try:
            for i in range(frames - 1):
                self.draw()
                plt.show()
                if interval:
                    sleep(interval)
                self.step()
                clear_output(wait=True)
            self.draw()
            plt.show()
        except KeyboardInterrupt:
            pass


def draw_array_2d(array, cmap='Blues', **options):
    n_rows, n_cols = array.shape
    options = underride(options,
                        cmap=cmap,
                        alpha=0.7,
                        vmin=0,
                        vmax=1,
                        interpolation='none',
                        origin='upper',
                        extent=[0, n_cols, 0, n_rows])

    ax.axis([0, n_cols, 0, n_rows])
    ax.set(xticks=[])
    ax.set(yticks=[])
    return ax.imshow(array, **options)


def make_life(n_rows, n_cols, pos_start=[1, 1], pattern='glider', *strings):
    life = Cell2D(n_rows, n_cols, mode='gol')

    patterns = {
        'glider': ['010', '001', '111'],
        'beehive': ['0110', '1001', '0110'],
        'toad': ['0111', '1110'],
        'rpent': ['011', '110', '010'],
        'glider_gun': [
            '000000000000000000000000100000000000',
            '000000000000000000000010100000000000',
            '000000000000110000001100000000000011',
            '000000000001000100001100000000000011',
            '110000000010000010001100000000000000',
            '110000000010001011000010100000000000',
            '000000000010000010000000100000000000',
            '000000000001000100000000000000000000',
            '000000000000110000000000000000000000'
        ]
    }

    strings = patterns.get(pattern)
    life.add_cells(pos_start[0], pos_start[1], *strings)
    return life


def read_life_file(filename, n_rows, n_cols, pos_start=[1, 1]):
    life = Cell2D(n_rows, n_cols, mode='gol')
    i = pos_start[0]
    with open(filename) as f:
        for line in f:
            if line.startswith('!'):
                continue
            line = line.strip()
            line = line.replace('O', '1')
            line = line.replace('.', '0')
            life.add_cells(i, pos_start[1], line)
            i += 1


def draw_rabbits(n_rows, n_cols):
    rabbits = ['1000111', '111001', '01']

    life = Cell2D(n_rows, n_cols, mode='gol')
    life.add_cells(n_rows // 2, n_cols // 2, *rabbits)
    life.animate(frames=100, interval=1)

    plt.show()


def draw_puffer_train(n_rows, n_cols):
    string1 = ['0001', '00001', '10001', '01111']
    string2 = ['1', '011', '001', '001', '01']

    life = Cell2D(n_rows, n_cols, mode='gol')
    col = 120
    life.add_cells(n_rows // 2 + 12, col, *string1)
    life.add_cells(n_rows // 2 + 26, col, *string1)
    life.add_cells(n_rows // 2 + 19, col, *string2)
    life.animate(frames=100, interval=1)

    plt.show()


def draw_replicator(n_rows):
    life = Cell2D(n_rows, mode='high')
    replicator = ['00111', '01001', '10001', '10010', '11100']
    life.add_cells(n_rows // 2, n_rows // 2, *replicator)
    life.animate(frames=200)


def underride(d, **options):
    for key, val in options.items():
        d.setdefault(key, val)
    return d
