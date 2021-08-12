import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from path_ring import make_ring_lattice


def rewire(G, p):
    nodes = set(G)
    for u, v in G.edges():
        if np.random.random() < p:
            choices = nodes - {u} - set(G[u])
            new_v = np.random.choice(list(choices))
            G.remove_edge(u, v)
            G.add_edge(u, new_v)


def make_ws_graph(n, k, p):
    ws = make_ring_lattice(n, k)
    rewire(ws, p)
    return ws


def draw(g, node_size=800, font_size=16):
    nx.draw(g,
            with_labels=True,
            pos=nx.circular_layout(g),
            node_color='red',
            node_size=node_size,
            font_color='white',
            font_size=font_size,
            font_weight='bold')


n = 10
k = 4
p = [0, 0.2, 1.0]

_, ax = plt.subplots()

for i in range(3):
    plt.subplot(1, 3, 1 + i)
    g = nx.random_graphs.watts_strogatz_graph(n, k, p[i])
    draw(g, node_size=200, font_size=12)
    ax.axis('equal')

plt.show()
