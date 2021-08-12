import numpy as np
import networkx as nx
from networkx.algorithms.approximation import average_clustering


def sample_path_lengths(G, nodes=None, trials=1000):
    if nodes is None:
        nodes = list(G)
    else:
        nodes = list(nodes)

    pairs = np.random.choice(nodes, (trials, 2))
    lengths = [nx.shortest_path_length(G, *pair) for pair in pairs]
    return lengths


def estimate_path_length(G, nodes=None, trials=1000):
    return np.mean(sample_path_lengths(G, nodes, trials))


def read_graph(filename):
    G = nx.Graph()
    array = np.loadtxt(filename, dtype=int)
    G.add_edges_from(array)
    return G


# https://snap.stanford.edu/data/facebook_combined.txt.gz
fb = read_graph('../../data/facebook_combined.txtz')
n, m = len(fb), len(fb.edges())  # (4039, 88234)

C = average_clustering(fb)
L = estimate_path_length(fb)
k = int(round(2 * m / n))  # 44

lattice = nx.watts_strogatz_graph(n, k, p=0)
len(lattice), len(lattice.edges())
# (4039, 88858)

C, average_clustering(lattice)
# (0.615, 0.747)
L, estimate_path_length(lattice)
# (3.717, 47.088)
