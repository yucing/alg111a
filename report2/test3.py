def bron_kerbosch(G, R, P, X):
  if not any((P, X)):
    yield R
  # 將 P 集合複製到新的集合 P2 中
  P2 = {v for v in P}
  # 遍歷 P2 集合
  for v in P2:
    bron_kerbosch(G, R + [v], P & G[v], X & G[v])
    # 將 v 從 P 中移除，並加入 X 中
    P.difference_update(v)
    X.update(v)

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
