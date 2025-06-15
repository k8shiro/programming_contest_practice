import networkx as nx
import matplotlib.pyplot as plt

# 無向グラフの作成
G = nx.Graph()

# ノードの追加
G.add_node(1)
G.add_nodes_from([2, 3, 4])

# エッジの追加（ノードも自動追加される）
G.add_edge(1, 2)
G.add_edges_from([(2, 3), (3, 4)])

# ノードとエッジの一覧表示
print("Nodes:", list(G.nodes))
print("Edges:", list(G.edges))

# ノード2の隣接ノード
print("Neighbors of 2:", list(G.neighbors(2)))

# 連結成分（無向グラフ）
components = list(nx.connected_components(G))
print("Connected Components:", components)

# ノード1から4までの最短経路
path = nx.shortest_path(G, source=1, target=4)
print("Shortest path from 1 to 4:", path)

# 各ノードの次数
degree_dict = dict(G.degree())
print("Degrees:", degree_dict)


