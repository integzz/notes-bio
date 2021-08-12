import numpy as np
import matplotlib.pyplot as plt


class GameOfLife(object):
    def __init__(self, cells_shape):
        # initial status
        self.colors = np.zeros(cells_shape)
        real_width = cells_shape[0] - 2
        real_height = cells_shape[1] - 2
        self.colors[1:-1,
                    1:-1] = np.random.randint(2,
                                              size=(real_width, real_height))
        self.timer = 0
        self.mask = np.ones(9)
        self.mask[4] = 0

    def update_state(self):
        new_colors = np.zeros(self.colors.shape)
        colors = self.colors
        for i in range(1, colors.shape[0] - 1):
            for j in range(1, colors.shape[0] - 1):
                # live cells number
                neighbor = colors[i - 1:i + 2, j - 1:j + 2].reshape((-1, ))
                neighbor_num = np.convolve(self.mask, neighbor, 'valid')[0]

                if neighbor_num == 3:
                    new_colors[i, j] = 1
                elif neighbor_num == 2:
                    new_colors[i, j] = colors[i, j]
                else:
                    new_colors[i, j] = 0
        self.colors = new_colors
        self.timer += 1

    def update_and_plot(self, n_iter, pause):
        plt.ion()
        for _ in range(n_iter):
            ax.set(title=f'Iter: {self.timer}')
            # binary plotting
            ax.imshow(self.colors)
            self.update_state()
            ax.pause(pause)
        plt.ioff()


if __name__ == '__main__':
    n = 60
    n_iter = 200
    pause = 1
    game = GameOfLife(cells_shape=(n, n))
    game.update_and_plot(n_iter, pause)
