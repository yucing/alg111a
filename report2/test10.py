import matplotlib.pyplot as plt
import networkx as nx

# 建立一個空的無向圖
G = nx.Graph()

# 加入圖中的結點
G.add_nodes_from(['1', '2', '3', '4', '5', '6', '7'])

# 加入圖中的邊
G.add_edges_from([('1', '2'), ('1', '3'), ('1', '4'), ('2', '3'), ('2', '4'),
                  ('3', '4'), ('2', '5'), ('4', '5'), ('5', '7'), ('4', '6')])

# 將圖畫出來
nx.draw(G, with_labels=True)

# 顯示圖形
plt.show()
