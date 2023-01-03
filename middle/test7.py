ans = []
def bron_kerbosch(G, R, P, X):
    #print('R=',R)
    #print('P=',P)
    #print('X=',X)
    if not any((P, X)):
        R = sorted(R)
        ans.append(R)
        for k in range(len(ans)-1):
            if R == ans[k]:
                ans.pop()
                break
        #print(ans)
    elif not any((P)) and any((X)):
        return
    else:
        P2 = [each_vertex for each_vertex in P]
        for each_vertex in P2:
            #print('each_vertex=',each_vertex)
            #print('G[each_vertex]=',G[each_vertex])
            #print('R+[each_vertex]=',R+[each_vertex])
            #print('P & G[each_vertex]=',P & G[each_vertex])
            #print('X & G[each_vertex]=',X & G[each_vertex])
            if not any((G[each_vertex])):
                break
            bron_kerbosch(G, R + [each_vertex], P & G[each_vertex], X & G[each_vertex])
            P.remove(each_vertex)
            X.add(each_vertex)
    


def find_cliques(G):
    for vertex in G:
        neighbors = G[vertex]
        bron_kerbosch(G, [vertex], neighbors, set())


G = {
  'A': set(['B', 'C']),
  'B': set(['A', 'C']),
  'C': set(['A', 'B']),
  'D': set(['C', 'E']),
  'E': set(['D'])
}

cliques = find_cliques(G)
#print(cliques)  # [['A', 'B', 'C'], ['C', 'D', 'E']]

print(ans)
