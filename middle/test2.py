def bron_kerbosch(G, R, P, X):
  if not any((P, X)):
    yield R
  for v in P:
    bron_kerbosch(G, R + [v], P & G[v], X & G[v])
    P.remove(v)
    X.add(v)

def find_cliques(G):
  for vertex in G:
    neighbors = G[vertex]
    for clique in bron_kerbosch(G, [vertex], neighbors, set()):
      yield clique

G = {
  'A': set(['B', 'C']),
  'B': set(['A', 'C']),
  'C': set(['A', 'B']),
  'D': set(['C', 'E']),
  'E': set(['D'])
}

cliques = [clique for clique in find_cliques(G)]
print(cliques)  # [['A', 'B', 'C'], ['C', 'D', 'E']]
