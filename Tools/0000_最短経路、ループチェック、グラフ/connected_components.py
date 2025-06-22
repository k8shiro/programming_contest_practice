"""
無効グラフの連結成分を求める例
"""

import networkx as nx

# グラフ作成（無向グラフ）
G = nx.Graph()
G.add_nodes_from(range(1, 11)) # ノード1〜10をあらかじめすべて追加
G.add_edges_from([
    (1, 2), (2, 3),    # このグループ1つ目
    (4, 5),            # グループ2つ目
    (6, 7), (7, 8), (8, 6)  # グループ3つ目（環）
])

# 連結成分ごとに分ける
components = list(nx.connected_components(G))

# 出力
for i, comp in enumerate(components, start=1):
    print(f"Component {i}: {comp}")

# 連結成分ごとにサブグラフを作成して表示
for component in nx.connected_components(G):
    subgraph = G.subgraph(component).copy()  # 独立したサブグラフにしたいならcopy()を付ける、変更しないなら不要
    print("Subgraph nodes:", list(subgraph.nodes()))
    print("Subgraph edges:", list(subgraph.edges()))