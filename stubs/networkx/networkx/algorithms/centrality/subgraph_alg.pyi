from networkx.utils.backends import _dispatch

@_dispatch
def subgraph_centrality_exp(G): ...
@_dispatch
def subgraph_centrality(G): ...
@_dispatch
def communicability_betweenness_centrality(G): ...
@_dispatch
def estrada_index(G): ...