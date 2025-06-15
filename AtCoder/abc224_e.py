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

from collections import defaultdict

def main():
    H, W, N = map(int, stdin.readline().strip().split())

    r_list = [[] for _ in range(H)]  # 各行にある (a, idx)
    c_list = [[] for _ in range(W)]  # 各列にある (a, idx)
    rc_list = []
    pos_map = dict()

    for _ in range(N):
        r, c, a = map(int, stdin.readline().strip().split())
        idx = (r - 1) * W + (c - 1)
        r -= 1
        c -= 1
        r_list[r].append((a, idx))
        c_list[c].append((a, idx))
        rc_list.append((a, idx))
        pos_map[idx] = (r, c)

    for r in range(H):
        r_list[r].sort(key=lambda x: x[0])
    for c in range(W):
        c_list[c].sort(key=lambda x: x[0])

    rc_list.sort(reverse=True)

    dp = [0] * (H * W)
    pending = defaultdict(list)

    i = 0
    while i < len(rc_list):
        a_now = rc_list[i][0]
        same_a = []

        while i < len(rc_list) and rc_list[i][0] == a_now:
            same_a.append(rc_list[i])
            i += 1

        temp_dp = dict()

        for _, idx in same_a:
            r, c = pos_map[idx]

            # r行から
            row = r_list[r]
            for x, j in reversed(row):
                if x <= a_now:
                    break
                temp_dp[idx] = max(temp_dp.get(idx, 0), dp[j] + 1)

            # c列から
            col = c_list[c]
            for x, j in reversed(col):
                if x <= a_now:
                    break
                temp_dp[idx] = max(temp_dp.get(idx, 0), dp[j] + 1)

        # temp_dpで更新（依存がないのでまとめて）
        for idx in temp_dp:
            dp[idx] = temp_dp[idx]

    rc_list_original = rc_list.copy()
    rc_list_original.sort()

    for a, idx in rc_list_original:
        print(dp[idx])


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
#     H, W, N = map(int, stdin.readline().strip().split())
    
#     r_list = [[] for _ in range(H)] # (a, idx)
#     c_list = [[] for _ in range(W)] 
#     rc_list = []
#     for _ in range(N):
#         r, c, a = map(int, stdin.readline().strip().split())
#         idx = (r - 1) * W + (c - 1)
#         r_list[r-1].append((a, idx))
#         c_list[c-1].append((a, idx))
#         rc_list.append((a, idx))

#     # 各行と列をソート
#     for r in range(H):
#         r_list[r].sort()
#     for c in range(W):
#         c_list[c].sort()
#     # 数値の大きい順にソート
#     rc_list_original = rc_list.copy()
#     rc_list.sort(reverse=True)

#     edges_a = {i: [] for i in range(H * W)}
#     edges_b = {i: [] for i in range(H * W)}
#     for r in range(H):
#         for i in range(len(r_list[r]) - 1):
#             #edges_a[r_list[r][i][1]] = r_list[r][i + 1:]
#             edges_a[r_list[r][i][1]] = (r, i+1)

#     for c in range(W):
#         for i in range(len(c_list[c]) - 1):
#             #edges_b[c_list[c][i][1]] = c_list[c][i + 1:]
#             edges_b[c_list[c][i][1]] = (c, i+1)

#     #print(edges)
#     dp = [0] * (H * W)
#     for a, idx in rc_list:
#         if edges_a[idx]:
#             r, i = edges_a[idx]
#             for next_a, next_idx in r_list[r][i:]:
#                 if next_a > a:
#                     dp[idx] = max(dp[next_idx] + 1, dp[idx])
#         if edges_b[idx]:
#             c, i = edges_b[idx]
#             for next_a, next_idx in c_list[c][i:]:
#                 if next_a > a:
#                     dp[idx] = max(dp[next_idx] + 1, dp[idx])

#     for a, idx in rc_list_original:
#         print(dp[idx])


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
#     H, W, N = map(int, stdin.readline().strip().split())
    
#     r_list = [[] for _ in range(H)] # (a, idx)
#     c_list = [[] for _ in range(W)] 
#     rc_list = []
#     for _ in range(N):
#         r, c, a = map(int, stdin.readline().strip().split())
#         idx = (r - 1) * W + (c - 1)
#         r_list[r-1].append((a, idx))
#         c_list[c-1].append((a, idx))
#         rc_list.append((a, idx))

#     # 各行と列をソート
#     for r in range(H):
#         r_list[r].sort()
#     for c in range(W):
#         c_list[c].sort()
#     # 数値の大きい順にソート
#     rc_list_original = rc_list.copy()
#     rc_list.sort(reverse=True)

#     edges_a = {i: [] for i in range(H * W)}
#     edges_b = {i: [] for i in range(H * W)}
#     for r in range(H):
#         for i in range(len(r_list[r]) - 1):
#             #edges_a[r_list[r][i][1]] = r_list[r][i + 1:]
#             edges_a[r_list[r][i][1]] = (r, i+1)

#     for c in range(W):
#         for i in range(len(c_list[c]) - 1):
#             #edges_b[c_list[c][i][1]] = c_list[c][i + 1:]
#             edges_b[c_list[c][i][1]] = (c, i+1)

#     #print(edges)
#     dp = [0] * (H * W)
#     for a, idx in rc_list:
#         if edges_a[idx]:
#             r, i = edges_a[idx]
#             for next_a, next_idx in r_list[r][i:]:
#                 if next_a > a:
#                     dp[idx] = max(dp[next_idx] + 1, dp[idx])
#         if edges_b[idx]:
#             c, i = edges_b[idx]
#             for next_a, next_idx in c_list[c][i:]:
#                 if next_a > a:
#                     dp[idx] = max(dp[next_idx] + 1, dp[idx])

#     for a, idx in rc_list_original:
#         print(dp[idx])








if __name__ == "__main__":
    main()


# WA
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
#     H, W, N = map(int, stdin.readline().strip().split())
#     masu = [[0] * W for _ in range(H)]
#     RC = []
#     for _ in range(N):
#         r, c, a = map(int, stdin.readline().strip().split())
#         masu[r-1][c-1] = a
#         RC.append((r-1, c-1))

#     edges = {i: [] for i in range(H * W)}
#     for r in range(H):
#         for c in range(W):
#             node_a = r * W + c
#             node_a_num = masu[r][c]
#             # 同じ行のチェック
#             for c2 in range(W):
#                 node_b = r * W + c2
#                 node_b_num = masu[r][c2]
#                 if node_a_num < node_b_num:
#                     edges[node_a].append(node_b)

#             # 同じ列のチェック
#             for r2 in range(H):
#                 node_b = r2 * W + c
#                 node_b_num = masu[r2][c]
#                 if node_a_num < node_b_num:
#                     edges[node_a].append(node_b)

#     # edgesをprint
#     # for key, val in edges.items():
#     #     print(f"{key}: {val}")

#     longest_paths = [-1] * (H * W)
#     def dfs(node):
#         if longest_paths[node] != -1:
#             return longest_paths[node]
        
#         if not edges[node]:
#             longest_paths[node] = 0
#             return 0

#         _count = -1
#         for next_node in edges[node]:
#             _count = max(_count, dfs(next_node) + 1)

#         longest_paths[node] = _count
#         return _count

#     for r, c in RC:
#         node = r * W + c
#         if longest_paths[node] == -1:
#             longest_paths[node] = dfs(node)

#     print(longest_paths)
    
#     for r, c in RC:
#         node = r * W + c
#         print(longest_paths[node])







# if __name__ == "__main__":
#     main()
