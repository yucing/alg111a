def bron_kerbosch(G, R, P, X):
    P2 = [each_vertex for each_vertex in P]
    for each_vertex in P2:
        #print('each_vertex=',each_vertex)
        #print('G[each_vertex]=',G[each_vertex])
        #print('R+[each_vertex]',R+[each_vertex])
        print('P & G[each_vertex]=',P & G[each_vertex])
        print('X & G[each_vertex]=',X & G[each_vertex])
        bron_kerbosch(G, R + [each_vertex], P & G[each_vertex], X & G[each_vertex])
        P.remove(each_vertex)
        X.add(each_vertex)
    if not any((P, X)):
        R = sorted(R)
        yield R
    

def find_cliques(G):
    clique = []
    for vertex in G:
        neighbors = G[vertex]
        clique = bron_kerbosch(G, [vertex], neighbors, set())
        yield clique
G = {
  'A': set(['B', 'C']),
  'B': set(['A', 'C']),
  'C': set(['A', 'B']),
  'D': set(['C', 'E']),
  'E': set(['D'])
}

cliques = find_cliques(G)
print(cliques)  # [['A', 'B', 'C'], ['C', 'D', 'E']]
