import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
from operator import itemgetter
from IPython.display import clear_output
from time import sleep


class Cell1D:
    def __init__(self, rule, n_rows=32, n_cols=None, string=None, anim=False):
        self.table, self.rule_bits = make_table(rule)
        if string:
            self.string = string
            self.n_cols = len(string)
            self.n_rows = self.n_cols
        else:
            self.n_rows = n_rows
            self.n_cols = 2 * n_rows + 1 if n_cols is None else n_cols
        self.array = np.zeros((self.n_rows, self.n_cols), dtype=np.int8)
        self.row_next = 0
        self.anim = anim
        self.rule = rule

    def start_middle(self):
        self.array[0, self.n_cols // 2] = 1
        self.row_next += 1

    def start_random(self):
        self.array[0] = np.random.random(self.n_cols).round()
        self.row_next += 1

    def start_string(self, s):
        # 由 Boolean 字符串生成
        self.array[0] = np.array([int(x) for x in s])
        self.row_next += 1

    def loop(self, steps=1):
        for i in range(steps):
            self.step()

    def step(self, animation=False):
        a = self.array
        i = self.row_next
        window = [4, 2, 1]
        # 'same'：输出与输入大小相同
        c = np.correlate(a[i - 1], window, mode='same')
        a[i] = self.table[c]
        if not self.anim:
            self.row_next += 1
        i = self.row_next - 1
        row = self.array[i]
        row[0], row[-1] = row[-2], row[1]

    def draw(self, frame=[0, None], **options):
        draw_array_1d(self.rule, self.n_rows)

    def animate(self, frames, interval=None, step=None, **options):
        if step is None:
            step = self.step
        plt.subplots()
        try:
            for i in range(self.n_rows - 2):
                self.draw(**options)
                plt.show()
                if interval:
                    sleep(interval)
                self.step()
                clear_output(wait=True)
            self.draw(**options)
            plt.show()
        except KeyboardInterrupt:
            pass

    def count_cells(self, mode=None):
        if not mode:
            self.start_middle()
        elif mode == 'random':
            self.start_random()
        elif mode == 'string':
            self.start_string(self.string)
        res = []
        for i in range(1, self.n_rows):
            cells = np.sum(self.array)
            res.append((i, i**2, cells))
            self.step()
        return res


def make_table(rule):
    rule = np.array([rule], dtype=np.uint8)
    rule_bits = np.unpackbits(rule)
    table = rule_bits[::-1]
    return table, rule_bits


def draw_array_1d(rule, n=32, mode=None, frame=[0, None], **options):
    ca = Cell1D(rule, n)
    if not mode:
        ca.start_middle()
    elif mode == 'random':
        ca.start_random()
    elif mode == 'string':
        ca.start_string(ca.string)
    ca.loop(n - 1)
    a = ca.array[:, frame[0]:frame[1]]
    ax.imshow(a, cmap='Blues', alpha=0.7)
    ax.set(xticks=[])
    ax.set(yticks=[])


def test_fractal_1d(rule, plot=True, ylabel='Number of Cells'):
    ca = Cell1D(rule, n_rows=500)
    res = ca.count_cells()
    steps, steps2, cells = zip(*res)
    if plot:
        options = dict(linestyle='dashed', color='gray', alpha=0.7)
        ax.plot(steps, steps2, label='d=2', **options)
        ax.plot(steps, cells, label='rule=%d' % rule)
        ax.plot(steps, steps, label='d=1', **options)

        ax.set(xscale='log',
               yscale='log',
               xlabel='Time Steps',
               ylabel=ylabel,
               xlim=(1, 600))
        ax.legend(loc='upper left')

    param_list = []
    for ys in [cells]:
        params = linregress(np.log(steps), np.log(ys))
        param_list.append(params[0])

    return param_list


def find_fractal_rules(d_range=[1.1, 1.9]):
    d = {}
    for rule in range(256):
        slope = test_fractal_1d(rule)[0]
        if d_range[0] < slope < d_range[1]:
            slope = np.around(slope, 3)
            if slope not in d:
                d[slope] = rule

    rules = []
    slopes = []
    for slope, rule in sorted(d.items(), key=itemgetter(1)):
        print(rule, slope)
        rules.append(rule)
        slopes.append(slope)
    return rules, slopes
