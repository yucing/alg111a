# Clique problem
## [clique problem](https://zh.m.wikipedia.org/zh-hant/%E5%88%86%E5%9C%98%E5%95%8F%E9%A1%8C)
* 圖論中的一個NP-complete問題
* clique 是一個途中兩兩相鄰的一個頂點集，或是一個完全子圖

![](https://github.com/yucing/alg111a/blob/main/picture/1.png)

# 程式由 Chat GPT 修改
# 暴力法
* 遍歷所有節點，並檢查是否為完全子圖
* 時間複雜度為O(n^2 * 2^n)，在大型圖中可能很慢
## 由 Chat GPT產生
### 程式
```py
def find_cliques(G):
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

```

### 輸出
```
[{'D', 'E'}, {'C', 'B', 'A'}, {'C', 'B', 'A'}, {'B', 'C', 'A'}]
```

### 問題
* 答案輸出重複
* ['C','D','E'] C與E沒有互相為鄰居，不太確認是否為答案

## 以下是更改後的程式
### 程式
```py
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
```
### 輸出
```
[['A', 'B', 'C']]
```

# Bron-Kerbosch 演算法
* 時間複雜度為O(3^(n/3))，比暴力解快上許多
## 由 Chat GPT產生
### 程式
```py
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

```
### 輸出
```
[]
```

### 問題
* 當求解的圖不是一個完全圖時，程式碼可能會回傳不正確的答案
* 因為 Bron-Kerbosch 演算法是假設輸入的圖是一個完全圖

## 以下是更改後的程式
### 程式
```py
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

```
### 輸出
```
[['A', 'B', 'C'], ['C', 'D'], ['D', 'E']]
```

# 圖形繪製
```py
import matplotlib.pyplot as plt
import networkx as nx

# 建立一個空的無向圖
G = nx.Graph()

# 加入圖中的結點
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

# 加入圖中的邊
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'D'), ('D', 'E')])

# 將圖畫出來
nx.draw(G, with_labels=True)

# 顯示圖形
plt.show()

```

# 參考資料
## [極大團算法](https://www.jianshu.com/p/437bd6936dad)