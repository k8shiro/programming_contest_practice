import heapq
from collections import defaultdict

def dijkstra(n, edges, start):
    """
    ダイクストラ法によって、startノードから各ノードへの
    最短距離と、その経路（直前ノード）を求める関数。

    :param n: ノード数（0〜n-1の整数ノードを想定）
    :param edges: エッジのリスト [(u, v, w), ...]
                  u→v に重みwの辺が存在することを表す（有向）
    :param start: 始点ノード
    :return: dist: 各ノードへの最短距離リスト
             prev: 経路復元のための前のノードを格納するリスト
    """

    # 隣接リスト形式でグラフを構築
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))  # u→v に重みwの辺

    # 各ノードへの距離を無限大で初期化
    dist = [float('inf')] * n
    dist[start] = 0  # 始点の距離は0

    # 最短経路を復元するための前ノード記録用リスト
    prev = [None] * n

    # 優先度付きキュー（距離, ノード）でスタート
    heap = [(0, start)]

    while heap:
        current_dist, u = heapq.heappop(heap)

        # 既により短い経路がわかっている場合はスキップ
        if current_dist > dist[u]:
            continue

        # 隣接ノードを確認
        for v, weight in graph[u]:
            new_dist = dist[u] + weight
            if new_dist < dist[v]:
                # より短い経路を発見した場合は更新
                dist[v] = new_dist
                prev[v] = u  # 経路復元用に前のノードを記録
                heapq.heappush(heap, (new_dist, v))

    return dist, prev

def reconstruct_path(prev, start, goal):
    """
    prevリストから、startからgoalまでの最短経路を復元する。

    :param prev: 各ノードの直前のノードを格納したリスト
    :param start: 始点ノード
    :param goal: 目的ノード
    :return: 経路をリストで返す（例: [start, ..., goal]）
    """
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = prev[current]
    path.reverse()  # ゴールからスタートまでを逆順にする

    # 到達不可能な場合は空リストを返す
    if path[0] != start:
        return []
    return path

if __name__ == "__main__":
    # ノード数（0〜4の5個）
    n = 5

    # グラフ定義：有向エッジ (from, to, weight)
    edges = [
        (0, 1, 10),
        (0, 2, 3),
        (1, 2, 1),
        (1, 3, 2),
        (2, 1, 4),
        (2, 3, 8),
        (2, 4, 2),
        (3, 4, 7),
        (4, 3, 9)
    ]

    start_node = 0  # 始点ノード

    # ダイクストラ法を実行
    dist, prev = dijkstra(n, edges, start_node)
    print(dist)
    print(prev)

    # 各ノードへの距離と経路を表示
    print(f"始点ノード: {start_node}")
    for goal in range(n):
        path = reconstruct_path(prev, start_node, goal)
        print(f"  ノード{goal}への最短距離: {dist[goal]}, 経路: {path}")
