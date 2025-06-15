"""
ワーシャル・フロイド法による最短経路計算と経路復元 
小規模・密なグラフに適したアルゴリズム
"""




INF = float('inf')

# n: ノードの数
# edges: エッジのリスト (u, v, w) 形式で、uからvへの重みwのエッジ(有向グラフ)
def floyd_warshall_with_path(n, edges):
    # 距離と経路行列の初期化
    dist = [[INF] * n for _ in range(n)]
    next_node = [[None] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0
        next_node[i][i] = i

    for u, v, w in edges:
        dist[u][v] = w
        next_node[u][v] = v  # u→vの次のノードはv

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    next_node[i][j] = next_node[i][k]  # 最短経路上の次のノード

    return dist, next_node

# 経路復元関数
def reconstruct_path(u, v, next_node):
    if next_node[u][v] is None:
        return []  # 経路なし
    path = [u]
    while u != v:
        u = next_node[u][v]
        path.append(u)
    return path


# グラフのエッジ (u, v, w) のリスト
# uからvへの重みwのエッジを表す
# 有効グラフ
# nodeは0から始まることに注意
n = 6 # ノードの数
edges = [
    (0, 1, 2), (0, 2, 5),
    (1, 2, 1), (1, 3, 2),
    (2, 3, 3), (3, 4, 1),
    (4, 5, 2), (5, 0, 4)
] 

dist, next_node = floyd_warshall_with_path(n, edges)
print(dist)
print(next_node)

# 最短距離行列の表示
print("距離行列:")
for row in dist:
    print(["INF" if x == float('inf') else x for x in row])

# 経路の復元例：0 → 5
u, v = 0, 5
path = reconstruct_path(u, v, next_node)
print(f"\nノード {u} から {v} への最短経路: {path}")
print(f"その距離: {dist[u][v]}")
