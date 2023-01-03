# Clique problem
## [clique problem](https://zh.m.wikipedia.org/zh-hant/%E5%88%86%E5%9C%98%E5%95%8F%E9%A1%8C)
* 圖論中的一個NP-complete問題
* clique 是一個途中兩兩相霖的一個頂點集，或是一個完全子圖

![](https://github.com/yucing/alg111a/blob/main/picture/1.png)

# 暴力法
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