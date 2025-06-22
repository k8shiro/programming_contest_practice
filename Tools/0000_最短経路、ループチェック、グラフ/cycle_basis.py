"""
無効グラフのサイクル部分を取得するためのコード
"""

import networkx as nx

# 無向グラフを定義
G = nx.Graph()
G.add_edges_from([
    (0, 1), (1, 2), (2, 0),  # 0-1-2 の三角形
    (1, 3), (3, 4), (4, 1)   # 1-3-4 の三角形
])

# サイクル基底を取得
cycles = nx.cycle_basis(G)
print("Cycles:", cycles)



# 無向グラフを定義
G = nx.Graph()
G.add_edges_from([
    (0, 1), (1, 2), (2, 0),  # 0-1-2 の三角形
    (0, 3), (2, 3)
])

# サイクル基底を取得
cycles = nx.cycle_basis(G)
print("Cycles:", cycles)