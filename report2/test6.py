def find_cliques(G):
    """使用暴力法尋找圖中的完全子圖。
    
    Args:
    - G: 一個字典，表示一個無向圖。字典的鍵表示圖中的結點，而字典的值則是一個集合，表示該結點的鄰居結點。
    
    Returns:
    一個生成器，產生所有完全子圖的集合。
    """
    # 取得圖中所有結點的集合
    nodes = set(G.keys())
    
    # 取得圖中所有結點的組合
    for i, u in enumerate(nodes):
        for v in list(nodes)[i+1:]:
            # 判斷 u 和 v 是否在同一個完全子圖中
            if u in G[v] and v in G[u]:
                # 取得 u 和 v 的共同鄰居
                common_neighbors = G[u] & G[v]
                
                # 檢查共同鄰居是否也在同一個完全子圖中
                if all(w in G[v] and w in G[u] for w in common_neighbors):
                    yield {u, v} | common_neighbors


G = {
  'A': set(['B', 'C']),
  'B': set(['A', 'C']),
  'C': set(['A', 'B']),
  'D': set(['C', 'E']),
  'E': set(['D'])
}

cliques = [clique for clique in find_cliques(G)]
print(cliques)  # [['A', 'B', 'C'], ['C', 'D', 'E']]
