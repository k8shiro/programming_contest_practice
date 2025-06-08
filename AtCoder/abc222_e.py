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

MOD = 998244353
def main():
    N, M, K = map(int, stdin.readline().strip().split())
    A = list(map(int, stdin.readline().strip().split()))
    A = [a - 1 for a in A]  # 0-indexedに変換

    edges = []
    path_count = {}
    for i in range(N-1):
        u, v = map(int, stdin.readline().strip().split())
        edges.append((u - 1, v - 1, 1))
        edges.append((v - 1, u - 1, 1))
        path_count[(min(u - 1, v - 1), max(u - 1, v - 1))] = 0

    n = N
    prev_list = []
    for start_node in range(n):
        dist, prev = dijkstra(n, edges, start_node)
        prev_list.append(tuple(prev))  # ミュータブルなリストをイミュータブルに変換


    pre = A[0]
    for a in A[1:]:
        path = reconstruct_path(prev_list[pre], pre, a)
        _pre = pre
        # print(pre, a, path)
        for p in path[1:]:
            l = min(_pre, p)
            r = max(_pre, p)
            path_count[(l, r)] += 1
            _pre = p
        pre = a

    # print(path_count)
    path_count_list = tuple(path_count.values())
    ans = solve(path_count_list, K)
    print(ans)



# R = (K+S) / 2 にする 
@lru_cache(None)
def solve(path_count_list, K):
    S = sum(path_count_list)
    if (K + S) % 2 != 0:
        return 0
    
    KS2 = (K + S) // 2

    dp = [0] * (KS2 + 1)
    dp[0] = 1  # 初期条件: 0の和を作る方法は1通り（何も選ばない）
    for count in path_count_list:
        for idx in range(KS2, count - 1, -1):
            dp[idx] = (dp[idx] + dp[idx - count]) % MOD

    return dp[KS2]  # K + S が偶数の場合の解





    
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

@lru_cache(None)
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
    main()

# TLE ワーシャル・フロイド法を使った
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

# MOD = 998244353
# def main():
#     N, M, K = map(int, stdin.readline().strip().split())
#     A = list(map(int, stdin.readline().strip().split()))
#     A = [a - 1 for a in A]  # 0-indexedに変換

#     edges = []
#     path_count = {}
#     for i in range(N-1):
#         u, v = map(int, stdin.readline().strip().split())
#         edges.append((u - 1, v - 1, 1))
#         edges.append((v - 1, u - 1, 1))
#         path_count[(min(u - 1, v - 1), max(u - 1, v - 1))] = 0

#     n = N
#     dist, next_node = floyd_warshall_with_path(n, edges)
#     next_node = tuple(tuple(row) for row in next_node)  # ミュータブルなリストをイミュータブルに変換
#     pre = A[0]
#     for a in A[1:]:
#         path = reconstruct_path(pre, a, next_node)
#         _pre = pre
#         # print(pre, a, path)
#         for p in path[1:]:
#             l = min(_pre, p)
#             r = max(_pre, p)
#             path_count[(l, r)] += 1
#             _pre = p
#         pre = a

#     # print(path_count)
#     path_count_list = list(path_count.values())


    
# INF = float('inf')
# def floyd_warshall_with_path(n, edges):
#     # 距離と経路行列の初期化
#     dist = [[INF] * n for _ in range(n)]
#     next_node = [[None] * n for _ in range(n)]

#     for i in range(n):
#         dist[i][i] = 0
#         next_node[i][i] = i

#     for u, v, w in edges:
#         dist[u][v] = w
#         next_node[u][v] = v  # u→vの次のノードはv

#     for k in range(n):
#         for i in range(n):
#             for j in range(n):
#                 if dist[i][k] + dist[k][j] < dist[i][j]:
#                     dist[i][j] = dist[i][k] + dist[k][j]
#                     next_node[i][j] = next_node[i][k]  # 最短経路上の次のノード

#     return dist, next_node

# # 経路復元関数
# @lru_cache(None)
# def reconstruct_path(u, v, next_node):
#     if next_node[u][v] is None:
#         return []  # 経路なし
#     path = [u]
#     while u != v:
#         u = next_node[u][v]
#         path.append(u)
#     return path



# if __name__ == "__main__":
#     main()
