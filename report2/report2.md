# Clique problem
# 極大團算法
## 參考資料
* [極大團算法](https://www.jianshu.com/p/437bd6936dad)
## Bron-Kerbosch 演算法
* 程式由Chat GPT修改

![](https://github.com/yucing/alg111a/blob/main/picture/1.png)

## 解題想法 - 參考極大團演算法
* 假設今有一圖如下，要求 Maxinal Clique

![](https://github.com/yucing/alg111a/blob/main/picture/10.png)

1. P 初始化所有節點，R 和 X 皆為空集合

![](https://github.com/yucing/alg111a/blob/main/picture/2.png)

2. 將 P 第一節點堆入 R 中，P 與 X 更新 (P: 更新為與推入節點相鄰的節點, X: 無動作)

![](https://github.com/yucing/alg111a/blob/main/picture/3.png)

3. 將 P 第一節點推入 R 中 (此時 R 有兩個節點)，P 與 X 更新 (P: 更新為與推入節點相鄰的節點, X: 無動作)

![](https://github.com/yucing/alg111a/blob/main/picture/4.png)

4. 重複相同動作， 此時 P 與 X 皆為空集合 -> Maximal Clique 產生

![](https://github.com/yucing/alg111a/blob/main/picture/5.png)

5. 以搜尋完{1,2}節點，因此回到上一層，從1搜尋到3，節點2為節點 1 與 3 的相鄰節點，但其以為極大圖的頂點，因此推入 X
6. X 不為空集合，因此{1,3}不為 Maximal Clique

![](https://github.com/yucing/alg111a/blob/main/picture/6.png)

7. 搜尋完節點 1 ，搜尋節點2，將節點2推入R，並更新P值(與節點2相鄰的節點)

![](https://github.com/yucing/alg111a/blob/main/picture/7.png)

8. 將P的第一個節點推入 R，更新 R 及 X，有一相鄰節點 1，但節點1以為極大圖節點，因此推入X
9. X 不為空集合，因此{2,3}不為 Maximal Clique

![](https://github.com/yucing/alg111a/blob/main/picture/8.png)

10. 搜尋完節點{2,3}，搜尋節點{2,4}，發現 P 及 X 皆為空集合 -> Maximal Clique 產生

![](https://github.com/yucing/alg111a/blob/main/picture/9.png)

```
{},{1,2,3,4,5,6,7},{}
    {1},{2,3,4},{}
        {1,2},{3,4},{}
            {1,2,3},{4},{}
                {1,2,3,4},{},{}-----Maximal Clique:{1,2,3,4}
            {1,2,4},{},{3}
        {1,3},{4},{2}
            {1,3,4},{},{2}
        {1,4},{},{2,3}
    {2},{3,4,5},{1}
        {2,3},{4},{1}
            {2,3,4},{},{1}
        {2,4},{5},{1}
            {2,4,5},{},{}-----Maximal Clique:{2,4,5}
        {2,5},{},{4}
    {3},{4},{1,2}
        {3,4},{},{1,2}
    {4},{5,6},{1,2,3}
        {4,5},{},{2}
        {4,6},{},{}-----Maximal Clique:{4,6}
    {5},{7},{2,4}
        {5,7},{0},{0}-----Maximal Clique:{5,7}
    {6},{},{4}
    {7},{},{5}
```

## 程式
```py
ans = []
def bron_kerbosch(G, R, P, X):
    #R=[] 已確定極大團頂點的陣列
    #P={v} 未處理頂點集合
    #X={} 以蒐過並屬於極大團的頂點集合
    if not any((P, X)):
        # 當 P and X 皆為空集合 Maximal Clique 產生
        R = sorted(R)
        ans.append(R)
    else:
        # 複製P，以免再刪除P時造成陣列變動
        P2 = [each_vertex for each_vertex in P]
        for each_vertex in P2:
            # R + [each_vertex] 將未處理頂點推入確定頂點陣列
            # P & G[each_vertex] each_vertex 連接的頂點
            # X & G[each_vertex] 確認是否有以是屬於極大團的頂點
            bron_kerbosch(G, R + [each_vertex], P & G[each_vertex], X & G[each_vertex])
            # 
            P.remove(each_vertex)
            X.add(each_vertex)
    


def find_cliques(G):
    a = set()
    # 建立頂點集合
    for vertex in G:
        a.add(vertex)
    bron_kerbosch(G, [], a, set())

# 頂點:set([連接的頂點])
G = {
  '1': set(['2','3','4']),
  '2': set(['1','3','4','5']),
  '3': set(['1','2','4']),
  '4': set(['1','2','3','5','6']),
  '5': set(['2','4','7']),
  '6': set(['4']),
  '7': set(['5'])
}


cliques = find_cliques(G)

print(ans)
```

## 輸出
```
R= []
P= {'1', '5', '7', '2', '6', '3', '4'}
X= set()
each_vertex= 1
G[each_vertex]= {'4', '3', '2'}
R+[each_vertex]= ['1']
P & G[each_vertex]= {'2', '3', '4'}
X & G[each_vertex]= set()
R= ['1']
P= {'2', '3', '4'}
X= set()
each_vertex= 2
G[each_vertex]= {'5', '1', '3', '4'}
R+[each_vertex]= ['1', '2']
P & G[each_vertex]= {'3', '4'}
X & G[each_vertex]= set()
R= ['1', '2']
P= {'3', '4'}
X= set()
each_vertex= 3
G[each_vertex]= {'1', '4', '2'}
R+[each_vertex]= ['1', '2', '3']
P & G[each_vertex]= {'4'}
X & G[each_vertex]= set()
R= ['1', '2', '3']
P= {'4'}
X= set()
each_vertex= 4
G[each_vertex]= {'1', '5', '2', '6', '3'}
R+[each_vertex]= ['1', '2', '3', '4']
P & G[each_vertex]= set()
X & G[each_vertex]= set()
R= ['1', '2', '3', '4']
P= set()
X= set()
Maximal Clique 產生
each_vertex= 4
G[each_vertex]= {'1', '5', '2', '6', '3'}
R+[each_vertex]= ['1', '2', '4']
P & G[each_vertex]= set()
X & G[each_vertex]= {'3'}
R= ['1', '2', '4']
P= set()
X= {'3'}
each_vertex= 3
G[each_vertex]= {'1', '4', '2'}
R+[each_vertex]= ['1', '3']
P & G[each_vertex]= {'4'}
X & G[each_vertex]= {'2'}
R= ['1', '3']
P= {'4'}
X= {'2'}
each_vertex= 4
G[each_vertex]= {'1', '5', '2', '6', '3'}
R+[each_vertex]= ['1', '3', '4']
P & G[each_vertex]= set()
X & G[each_vertex]= {'2'}
R= ['1', '3', '4']
P= set()
X= {'2'}
each_vertex= 4
G[each_vertex]= {'1', '5', '2', '6', '3'}
R+[each_vertex]= ['1', '4']
P & G[each_vertex]= set()
X & G[each_vertex]= {'3', '2'}
R= ['1', '4']
P= set()
X= {'3', '2'}
each_vertex= 5
G[each_vertex]= {'7', '4', '2'}
R+[each_vertex]= ['5']
P & G[each_vertex]= {'2', '7', '4'}
X & G[each_vertex]= set()
R= ['5']
P= {'2', '7', '4'}
X= set()
each_vertex= 2
G[each_vertex]= {'5', '1', '3', '4'}
R+[each_vertex]= ['5', '2']
P & G[each_vertex]= {'4'}
X & G[each_vertex]= set()
R= ['5', '2']
P= {'4'}
X= set()
each_vertex= 4
G[each_vertex]= {'1', '5', '2', '6', '3'}
R+[each_vertex]= ['5', '2', '4']
P & G[each_vertex]= set()
X & G[each_vertex]= set()
R= ['5', '2', '4']
P= set()
X= set()
Maximal Clique 產生
each_vertex= 7
G[each_vertex]= {'5'}
R+[each_vertex]= ['5', '7']
P & G[each_vertex]= set()
X & G[each_vertex]= set()
R= ['5', '7']
P= set()
X= set()
Maximal Clique 產生
each_vertex= 4
G[each_vertex]= {'1', '5', '2', '6', '3'}
R+[each_vertex]= ['5', '4']
P & G[each_vertex]= set()
X & G[each_vertex]= {'2'}
R= ['5', '4']
P= set()
X= {'2'}
each_vertex= 7
G[each_vertex]= {'5'}
R+[each_vertex]= ['7']
P & G[each_vertex]= set()
X & G[each_vertex]= {'5'}
R= ['7']
P= set()
X= {'5'}
each_vertex= 2
G[each_vertex]= {'5', '1', '3', '4'}
R+[each_vertex]= ['2']
P & G[each_vertex]= {'3', '4'}
X & G[each_vertex]= {'5', '1'}
R= ['2']
P= {'3', '4'}
X= {'5', '1'}
each_vertex= 3
G[each_vertex]= {'1', '4', '2'}
R+[each_vertex]= ['2', '3']
P & G[each_vertex]= {'4'}
X & G[each_vertex]= {'1'}
R= ['2', '3']
P= {'4'}
X= {'1'}
each_vertex= 4
G[each_vertex]= {'1', '5', '2', '6', '3'}
R+[each_vertex]= ['2', '3', '4']
P & G[each_vertex]= set()
X & G[each_vertex]= {'1'}
R= ['2', '3', '4']
P= set()
X= {'1'}
each_vertex= 4
G[each_vertex]= {'1', '5', '2', '6', '3'}
R+[each_vertex]= ['2', '4']
P & G[each_vertex]= set()
X & G[each_vertex]= {'5', '1', '3'}
R= ['2', '4']
P= set()
X= {'5', '1', '3'}
each_vertex= 6
G[each_vertex]= {'4'}
R+[each_vertex]= ['6']
P & G[each_vertex]= {'4'}
X & G[each_vertex]= set()
R= ['6']
P= {'4'}
X= set()
each_vertex= 4
G[each_vertex]= {'1', '5', '2', '6', '3'}
R+[each_vertex]= ['6', '4']
P & G[each_vertex]= set()
X & G[each_vertex]= set()
R= ['6', '4']
P= set()
X= set()
Maximal Clique 產生
each_vertex= 3
G[each_vertex]= {'1', '4', '2'}
R+[each_vertex]= ['3']
P & G[each_vertex]= {'4'}
X & G[each_vertex]= {'1', '2'}
R= ['3']
P= {'4'}
X= {'1', '2'}
each_vertex= 4
G[each_vertex]= {'1', '5', '2', '6', '3'}
R+[each_vertex]= ['3', '4']
P & G[each_vertex]= set()
X & G[each_vertex]= {'1', '2'}
R= ['3', '4']
P= set()
X= {'1', '2'}
each_vertex= 4
G[each_vertex]= {'1', '5', '2', '6', '3'}
R+[each_vertex]= ['4']
P & G[each_vertex]= set()
X & G[each_vertex]= {'1', '5', '2', '6', '3'}
R= ['4']
P= set()
X= {'1', '5', '2', '6', '3'}
[['1', '2', '3', '4'], ['2', '4', '5'], ['5', '7'], ['4', '6']]
```