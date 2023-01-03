output = []

def find_cliques(i):
    nodes=G[i]
    out = []
    for index, items in enumerate(list(nodes)):
        #print(i,items) # 
        for v in list(nodes)[index+1:]:
            if items in G[v] and v in G[items]:
                common_neighbors = G[items] & G[v]

                if all(w in G[v] and w in G[items] for w in common_neighbors):
                    out.append(i)
                    out.append(v)
                    out.append(items)
    out = sorted(out)
    if out != []:
        output.append(out)
        for k in range(len(output)-1):
            if out == output[k]:
                output.pop()
                break

G = {
  'A': set(['B', 'C']),
  'B': set(['A', 'C']),
  'C': set(['A', 'B']),
  'D': set(['C', 'E']),
  'E': set(['D'])
}

for i in G:
    find_cliques(i)

print(output)