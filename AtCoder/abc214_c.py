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
    N = int(stdin.readline().strip())
    S = list(map(int, stdin.readline().split()))
    T = list(map(int, stdin.readline().split()))

    graph = { i: [] for i in range(N+1) }

    for idx, t in enumerate(T):
        graph[0].append((idx + 1, t))
    for idx, s in enumerate(S):
        idx += 1  # 1-indexedにするため
        next_idx = idx + 1 if idx + 1 <= N else 1
        graph[idx].append((next_idx, s))

    result = dijkstra(graph, 0)
    
    for idx in range(1, N + 1):
        print(result[idx])

    
 


import heapq  # 優先度付きキュー（最小ヒープ）を使うための標準モジュール

def dijkstra(graph, start):
    """
    ダイクストラ法を使って、スタートノードから他のすべてのノードへの
    最短距離を求める関数。

    :param graph: 各ノードとその隣接ノード・重みを辞書形式で表したグラフ
                  例: {'A': [('B', 2), ('C', 5)], 'B': [('C', 1)]}
    :param start: 探索を開始するノード（例: 'A'）
    :return: 各ノードへの最短距離を格納した辞書
    """

    # 各ノードへの最短距離を記録する辞書（初期値はすべて無限大）
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # スタートノードへの距離は 0

    # 探索キュー（(距離, ノード) のタプル）を優先度付きキューとして使う
    queue = [(0, start)]  # 初期状態としてスタートノードを追加

    # キューが空になるまでループ
    while queue:
        # 最も距離が短いノードを取り出す
        current_distance, current_node = heapq.heappop(queue)

        # 既に発見済みのより短い距離があればスキップ
        if current_distance > distances[current_node]:
            continue

        # 現在のノードに隣接するノードを調べる
        for neighbor, weight in graph[current_node]:
            # 現在の距離 + このエッジの重み を仮の距離とする
            distance = current_distance + weight

            # より短い距離が見つかった場合は更新
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                # キューに追加（まだ探索していないが、今後取り出すため）
                heapq.heappush(queue, (distance, neighbor))

    # 最終的な距離マップを返す
    return distances

if __name__ == "__main__":
    main()


# TLE
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
#     N = int(stdin.readline().strip())
#     S = list(map(int, stdin.readline().split()))
#     T = list(map(int, stdin.readline().split()))


#     MIN_TIMES = T[:]
#     for s_idx in range(N):
#         _s_idx = s_idx
#         s_time = T[s_idx]
#         while True:
#             s_time += S[s_idx]
#             next_s_idx = (s_idx + 1) % N
#             MIN_TIMES[next_s_idx] = min(MIN_TIMES[next_s_idx], s_time)

#             s_idx = next_s_idx
#             if s_idx == _s_idx:
#                 break
    
#     for t in MIN_TIMES:
#         print(t)
    
 

# if __name__ == "__main__":
#     main()
