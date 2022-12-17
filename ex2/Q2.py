import networkx as nx
import numpy as np

def find_k_cliques(G, k):
    k_cliques = []
    for clique in nx.find_cliques(G):
        if len(clique) == k:
            k_cliques.append(set(clique))
    return k_cliques


def generate_overlap_matrix(cliques, k):
    n = len(cliques)
    mat = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            intersection_size = len(cliques[i] & cliques[j])
            if i != j and intersection_size == k - 1:
                mat[i][j] = 1
                mat[j][i] = 1
            if i == j and intersection_size == k:
                mat[i][i] = 1
    return mat


def get_communities_from_connected_components(k_cliques, connected_components):
    cliques_from_connected_components = [[k_cliques[i] for i in component] for component in connected_components]
    communities = [set().union(*clique_component) for clique_component in cliques_from_connected_components]
    return communities


def find_k_clique_communities(G, k):
    k_cliques = find_k_cliques(G, k)
    overlap_mat = generate_overlap_matrix(k_cliques, k)
    overlap_graph = nx.from_numpy_matrix(overlap_mat)
    connected_components = nx.connected_components(overlap_graph)
    communities = get_communities_from_connected_components(k_cliques, connected_components)
    return communities
