import numpy as np
from scipy.special import comb
from path_ring import make_ring_lattice
from graph_random import all_pairs_undirected
'''
`clustering_coefficient`为每个节点调用`node_clustering`一次。`node_clustering`是以$k$为单位的二次函数，即邻居数。因此：
- 在完整图中，$k = n-1$，所以`node_clustering`是$O(n^2)$，且`clustering_coefficient`是$O(n^3)$。
- 在环形晶格或其他图中，$k$与$n$不成正比的图，`clustering_coefficient`是$O(k^2 n)$。
'''


def node_clustering(G, u):
    neighbors = G[u]
    k = len(neighbors)
    if k < 2:
        return np.nan

    possible = comb(k, 2)
    exist = 0
    for v, w in all_pairs_undirected(neighbors):
        if G.has_edge(v, w):
            exist += 1
    return exist / possible


lattice = make_ring_lattice(10, 4)
node_clustering(lattice, 1)  # 0.5


def clustering_coefficient(G):
    cu = [node_clustering(G, node) for node in G]
    return np.nanmean(cu)


clustering_coefficient(lattice)  # 0.5
