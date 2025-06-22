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
    N, M = map(int, stdin.readline().strip().split())
    import networkx as nx
    G = nx.Graph()
    for _ in range(M):
        u, v = map(int, stdin.readline().strip().split())
        G.add_edge(u, v)


    # 連結成分を取得
    count = 0
    for component in nx.connected_components(G):
        subgraph = G.subgraph(component)
        node_num = subgraph.number_of_nodes()
        edge_num = subgraph.number_of_edges()
        if edge_num != node_num:
            print(0)
            return

        count += 1





    ans = 2 ** count
    print(ans % MOD)

    
if __name__ == "__main__":
    main()


# dfsでもTLE
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
#     N, M = map(int, stdin.readline().strip().split())
#     UV = []
#     for _ in range(M):
#         u, v = map(int, stdin.readline().strip().split())
#         UV.append((u, v))

#     ans = dfs(0, set(), UV, N)
#     print(ans % MOD)

# def dfs(idx, visited, UV, N):
#     if idx == len(UV):
#         if len(visited) == N:
#             return 1
#         else:
#             return 0

#     u, v = UV[idx]
#     count = 0
#     if u not in visited:
#         visited.add(u)
#         count += dfs(idx + 1, visited, UV, N)
#         count %= MOD
#         visited.remove(u)
#     if v not in visited:
#         visited.add(v)
#         count += dfs(idx + 1, visited, UV, N)
#         count %= MOD
#         visited.remove(v)
#     return count


# if __name__ == "__main__":
#     main()

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

# MOD = 998244353
# def main():
#     N, M = map(int, stdin.readline().strip().split())
#     UV = []
#     for _ in range(M):
#         u, v = map(int, stdin.readline().strip().split())
#         UV.append((u, v))

#     from itertools import product
#     bitstrings = product((0, 1), repeat=M)
#     count = 0
#     for bits in bitstrings:
#         nodes = set()
#         for idx, bit in enumerate(bits):
#             if UV[idx][bit] in nodes:
#                 break
#             nodes.add(UV[idx][bit])
#         if len(nodes) == N:
#             count += 1
#             count %= MOD
#     print(count)


# if __name__ == "__main__":
#     main()
