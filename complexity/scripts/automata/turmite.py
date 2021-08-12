import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon
import cell2d


class Turmite(cell2d.Cell2D):
    direction = {
        0: (-1, 0),  # north
        1: (0, 1),  # east
        2: (1, 0),  # south
        3: (0, -1)
    }  # west

    def __init__(self, n_rows, n_cols=None):
        n_cols = n_rows if n_cols is None else n_cols
        self.array = np.zeros((n_rows, n_cols), np.uint8)
        self.loc = np.array([n_rows // 2, n_cols // 2])
        self.state = 0

    def step(self):
        loc = tuple(self.loc)
        # get the state of the current cell
        try:
            cell = self.array[loc]
        except IndexError:
            raise IndexError('The turmite has gone off the grid')

        # toggle the current cell
        self.array[loc] ^= 1

        if cell:
            # turn left
            self.state = (self.state + 3) % 4
        else:
            # turn right
            self.state = (self.state + 1) % 4

        direction = self.direction[self.state]
        self.loc += direction

    def draw(self):
        super().draw()

        # draw the arrow
        center, direction = self.arrow_specs()
        self.arrow = RegularPolygon(center,
                                    3,
                                    color='orange',
                                    radius=0.4,
                                    direction=direction)
        ax = plt.gca()
        ax.add_patch(self.arrow)

    def arrow_specs(self):
        a = self.array
        n_rows, n_cols = a.shape
        i, j = self.loc
        center = j + 0.5, n_rows - i - 0.5
        direction = -np.pi / 2 * self.state
        return center, direction
