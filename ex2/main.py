import networkx as nx
def newman_girvan(graph, k):
  # Create a list of all the edges in the graph
  edges = [(u, v) for u, v in graph.edges()]

  # Initialize a list to store the communities
  communities = []

  # Repeat until there are no more edges in the graph
  while len(edges) > 0 and len(communities) < k:
    # Find the edge with the highest betweenness centrality
    e = max(edges, key=lambda x: nx.edge_betweenness_centrality(graph)[x])

    # Remove the edge from the graph
    graph.remove_edge(*e)

    # Find all the connected components in the graph
    communities = list(nx.connected_components(graph))

  # Return the communities
  return communities
