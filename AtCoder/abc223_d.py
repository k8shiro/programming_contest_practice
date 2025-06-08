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
    graph = {i: [] for i in range(1, N + 1)}
    

    for _ in range(M):
        a, b = map(int, stdin.readline().strip().split())
        graph[a].append(b)

    order = lex_smallest_toposort(graph)
    if order:
        print(*order)
    else:
        print(-1)
    



import heapq
from typing import Dict, List, Any

def lex_smallest_toposort(graph: Dict[Any, List[Any]]) -> List[Any]:
    """
    辞書順最小のトポロジカル順序を1つ返す（閉路があると空リスト）

    Args:
        graph (dict): 隣接リスト形式の有向グラフ

    Returns:
        List[Any]: 辞書順最小のトポロジカル順序 or []（閉路あり）
    """

    # すべてのノードを抽出
    nodes = set(graph.keys())
    for neighbors in graph.values():
        nodes.update(neighbors)

    # 入次数の初期化
    in_degree = {node: 0 for node in nodes}
    for u in graph:
        for v in graph[u]:
            in_degree[v] += 1

    # 入次数0のノードをmin-heapに追加
    heap = [node for node in nodes if in_degree[node] == 0]
    heapq.heapify(heap)

    result = []

    while heap:
        node = heapq.heappop(heap)
        result.append(node)
        for neighbor in graph.get(node, []):
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                heapq.heappush(heap, neighbor)

    # 閉路がある場合
    if len(result) != len(nodes):
        return []

    return result





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
#     N, M = map(int, stdin.readline().strip().split())

#     nodes = {}
#     for i in range(1, N + 1):
#         nodes[i] = {'oya': set(), 'ko': set()}

#     for _ in range(M):
#         a, b = map(int, stdin.readline().strip().split())
#         nodes[a]['ko'].add(b)
#         nodes[b]['oya'].add(a)

#     # print(nodes)
#     ANS = []
#     while True:
#         flag = False
#         to_delete = []
#         for key, val in nodes.items():
#             if not val['oya']:
#                 ANS.append(key)
#                 for ko in val['ko']:
#                     nodes[ko]['oya'].discard(key)
#                 to_delete.append(key)
#                 flag = True
#                 break
#         for key in to_delete:
#             del nodes[key]

#         if not nodes:
#             break

#         if not flag:
#             print(-1)
#             return

#     print(*ANS)



# if __name__ == "__main__":
#     main()
