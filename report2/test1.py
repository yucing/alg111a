def bron_kerbosch(G, R, P, X):
  # 如果 P 和 X 都是空集合，則印出 R 中的所有結點
  if not any((P, X)):
    yield R
  # 從 P 中的所有結點中遍歷
  for v in P:
    # 遞迴呼叫 bron_kerbosch，並將 v 加入 R 中，
    # 並將 P 中與 v 相鄰且不在 X 中的結點加入 P 中
    # 並將 X 中與 v 相鄰的結點加入 X 中
    bron_kerbosch(G, R + [v], P & G[v], X & G[v])
    # 將 v 從 P 中移除，並加入 X 中
    P.remove(v)
    X.add(v)

def find_cliques(G):
  # 遍歷 G 中的所有結點
  for vertex in G:
    neighbors = G[vertex]
    # 對於每個結點，呼叫 bron_kerbosch 來尋找完全子圖
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
