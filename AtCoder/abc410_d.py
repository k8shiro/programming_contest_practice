
from sys import stdin

# 再帰の深さ制限を変更
import sys
sys.setrecursionlimit(10**6)

from decimal import Decimal

# メモ化
from functools import lru_cache

# 探索失敗用にINT_MAXを定義
INT_MAX = 10**18

# 10^9 + 7
MOD = 10**9 + 7


def main():
    N, M = map(int, stdin.readline().strip().split())

    graph = {i: [] for i in range(1, N+1)}

    for _ in range(M):
        a, b, w = map(int, stdin.readline().strip().split())
        graph[a].append((b, w))

    from collections import deque
    MAX_XOR = float('inf')
    visited = [set() for _ in range(N + 1)]

    queue = deque()
    queue.append((1, 0))  # (node, current_xor)
    visited[1].add(0)

    while queue:
        current_node, current_xor = queue.popleft()

        for neighbor, weight in graph[current_node]:
            new_xor = current_xor ^ weight
            if new_xor not in visited[neighbor]:
                visited[neighbor].add(new_xor)
                queue.append((neighbor, new_xor))

    if visited[N]:
        print(min(visited[N]))
    else:
        print(-1)

    




if __name__ == "__main__":
    main()

# from sys import stdin

# # 再帰の深さ制限を変更
# import sys
# sys.setrecursionlimit(10**6)

# from decimal import Decimal

# # メモ化
# from functools import lru_cache

# # 探索失敗用にINT_MAXを定義
# INT_MAX = 10**18

# # 10^9 + 7
# MOD = 10**9 + 7


# def main():
#     N, M = map(int, stdin.readline().strip().split())

#     graph = {i: [] for i in range(1, N+1)}

#     for _ in range(M):
#         a, b, w = map(int, stdin.readline().strip().split())
#         graph[a].append((b, w))

#     result = dijkstra(graph, 1)
#     if result[N] == float('inf'):
#         print(-1)
#     else:
#         print(result[N])


# import heapq
# def dijkstra(graph, start):
#     """
#     ダイクストラ法を使って、スタートノードから他のすべてのノードへの
#     最短距離を求める関数。

#     :param graph: 各ノードとその隣接ノード・重みを辞書形式で表したグラフ
#                   例: {'A': [('B', 2), ('C', 5)], 'B': [('C', 1)]}
#     :param start: 探索を開始するノード（例: 'A'）
#     :return: 各ノードへの最短距離を格納した辞書
#     """

#     # 各ノードへの最短距離を記録する辞書（初期値はすべて無限大）
#     distances = {node: float('inf') for node in graph}
#     distances[start] = 0  # スタートノードへの距離は 0

#     # 探索キュー（(距離, ノード) のタプル）を優先度付きキューとして使う
#     queue = [(0, start)]  # 初期状態としてスタートノードを追加

#     # キューが空になるまでループ
#     while queue:
#         # ノードを取り出す
#         current_distance, current_node = heapq.heappop(queue)

#         # 既に発見済みのより短い距離があればスキップ
#         # if current_distance > distances[current_node]:
#         #     continue

#         # 現在のノードに隣接するノードを調べる
#         for neighbor, weight in graph[current_node]:
#             # 現在の距離 + このエッジの重み を仮の距離とする
#             distance = current_distance ^ weight

#             # より短い距離が見つかった場合は更新
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 # キューに追加（まだ探索していないが、今後取り出すため）
#                 heapq.heappush(queue, (distance, neighbor))

#     # 最終的な距離マップを返す
#     return distances

    




# if __name__ == "__main__":
#     main()






# from sys import stdin

# # 再帰の深さ制限を変更
# import sys
# sys.setrecursionlimit(10**6)

# from decimal import Decimal

# # メモ化
# from functools import lru_cache

# # 探索失敗用にINT_MAXを定義
# INT_MAX = 10**18

# # 10^9 + 7
# MOD = 10**9 + 7


# def main():
#     N, M = map(int, stdin.readline().strip().split())

#     graph = {i: [] for i in range(1, N+1)}

#     for _ in range(M):
#         a, b, w = map(int, stdin.readline().strip().split())
#         graph[a].append((b, w))

#     result = dijkstra(graph, 1)
#     if result[N] == float('inf'):
#         print(-1)
#     else:
#         print(result[N])


# import heapq
# def dijkstra(graph, start):
#     """
#     ダイクストラ法を使って、スタートノードから他のすべてのノードへの
#     最短距離を求める関数。

#     :param graph: 各ノードとその隣接ノード・重みを辞書形式で表したグラフ
#                   例: {'A': [('B', 2), ('C', 5)], 'B': [('C', 1)]}
#     :param start: 探索を開始するノード（例: 'A'）
#     :return: 各ノードへの最短距離を格納した辞書
#     """

#     # 各ノードへの最短距離を記録する辞書（初期値はすべて無限大）
#     distances = {node: float('inf') for node in graph}
#     distances[start] = 0  # スタートノードへの距離は 0

#     # 探索キュー（(距離, ノード) のタプル）を優先度付きキューとして使う
#     queue = [(0, start)]  # 初期状態としてスタートノードを追加

#     # キューが空になるまでループ
#     while queue:
#         # ノードを取り出す
#         current_distance, current_node = heapq.heappop(queue)

#         # 既に発見済みのより短い距離があればスキップ
#         if current_distance > distances[current_node]:
#             continue

#         # 現在のノードに隣接するノードを調べる
#         for neighbor, weight in graph[current_node]:
#             # 現在の距離 + このエッジの重み を仮の距離とする
#             distance = current_distance ^ weight

#             # より短い距離が見つかった場合は更新
#             if distance < distances[neighbor]:
#                 distances[neighbor] = distance
#                 # キューに追加（まだ探索していないが、今後取り出すため）
#                 heapq.heappush(queue, (distance, neighbor))

#     # 最終的な距離マップを返す
#     return distances

    




# if __name__ == "__main__":
#     main()
