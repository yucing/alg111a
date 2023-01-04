ans = []
def bron_kerbosch(G, R, P, X):
    #print('R=',R)
    #print('P=',P)
    #print('X=',X)
    if not any((P, X)):
        R = sorted(R)
        ans.append(R)
    else:
        P2 = [each_vertex for each_vertex in P]
        for each_vertex in P2:
            #print('each_vertex=',each_vertex)
            #print('G[each_vertex]=',G[each_vertex])
            #print('R+[each_vertex]=',R+[each_vertex])
            #print('P & G[each_vertex]=',P & G[each_vertex])
            #print('X & G[each_vertex]=',X & G[each_vertex])
            bron_kerbosch(G, R + [each_vertex], P & G[each_vertex], X & G[each_vertex])
            P.remove(each_vertex)
            X.add(each_vertex)
    


def find_cliques(G):
    a = set()
    for vertex in G:
        a.add(vertex)
    bron_kerbosch(G, [], a, set())


G = {
  '1': set(['2','3']),
  '2': set(['1','3','4']),
  '3': set(['1','2']),
  '4': set(['2']),
}


cliques = find_cliques(G)

print(ans)