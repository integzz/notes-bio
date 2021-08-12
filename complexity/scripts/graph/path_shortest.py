import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from path_ring import make_ring_lattice


def path_lengths(G):
    length_iter = nx.shortest_path_length(G)
    for _, dist_map in length_iter:
        for _, dist in dist_map.items():
            yield dist


def characteristic_path_length(G):
    return np.mean(list(path_lengths(G)))


complete = nx.complete_graph(10)
characteristic_path_length(complete)  # 0.9
lattice = make_ring_lattice(1000, 10)
characteristic_path_length(lattice)  # 50.4
