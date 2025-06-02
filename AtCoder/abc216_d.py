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

    from collections import deque
    tutu = []

    for m in range(M):
        k = int(stdin.readline().strip())
        a = list(map(int, stdin.readline().strip().split()))
        queue = deque(a)
        tutu.append(queue)

    # 先頭の色をメモ
    top_colors = [-1] * (N + 1)
    del_indexs = deque()

    for m in range(M):
        top = tutu[m][0]
        if top_colors[top] != -1:
            del_indexs.append((m, top_colors[top]))
            top_colors[top] = -1
        else:
            top_colors[top] = m

    # 削除を続ける
    while del_indexs:
        idx_1, idx_2 = del_indexs.popleft()

        # idx_1を処理
        tutu[idx_1].popleft()
        if tutu[idx_1]:
            top = tutu[idx_1][0]
            if top_colors[top] != -1:
                del_indexs.append((idx_1, top_colors[top]))
                top_colors[top] = -1
            else:
                top_colors[top] = idx_1

        # idx_2を処理
        tutu[idx_2].popleft()
        if tutu[idx_2]:
            top = tutu[idx_2][0]
            if top_colors[top] != -1:
                del_indexs.append((idx_2, top_colors[top]))
                top_colors[top] = -1
            else:
                top_colors[top] = idx_2

    # 筒に残りがあるか確認
    ans = True
    for m in range(M):
        if tutu[m]:
            ans = False
            break
    if ans:
        print("Yes")
    else:
        print("No")


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
#     graph = {color: set() for color in range(N)}

#     import networkx as nx
#     G = nx.DiGraph()

#     for m in range(M):
#         k = int(stdin.readline().strip())
#         a = list(map(int, stdin.readline().strip().split()))
#         for idx, top_a in enumerate(a):
#             for botom_a in a[idx + 1:]:
#                 G.add_edge(botom_a-1, top_a-1)

#     ans = nx.is_directed_acyclic_graph(G)
#     if ans:
#         print("Yes")
#     else:
#         print("No")




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


# BALL_POS = dict()
# A = []
# CACHE = set()

# def main():
#     global BALL_POS, A

#     N, M = map(int, stdin.readline().strip().split())
#     for m in range(M):
#         k = int(stdin.readline().strip())
#         a = list(map(int, stdin.readline().strip().split()))
#         A.append(a)
#         for idx, _a in enumerate(a):
#             if _a not in BALL_POS:
#                 BALL_POS[_a] = [(m, idx)]
#             else:
#                 BALL_POS[_a].append((m, idx))

#     # print(BALL_POS)

#     ans = True
#     for color in range(1, N + 1):
#         ans = ans and check(color)
#     if ans:
#         print("Yes")
#     else:
#         print("No")


# @lru_cache(maxsize=None)
# def check(color):
#     global BALL_POS, A, CACHE
#     if color in CACHE:
#         return False
#     CACHE.add(color)
#     ball_pos_a = BALL_POS[color][0]
#     ball_pos_b = BALL_POS[color][1]

#     # 同じ箱にある場合
#     if ball_pos_a[0] == ball_pos_b[0]:
#         return False

#     # 異なる箱にある場合
#     # 自分より前のボールが取り出せるか、自分が先頭なら取り出せる
#     ball_a_flag = True
#     if ball_pos_a[1] == 0:
#         ball_a_flag = True
#     else:
#         for color in A[ball_pos_a[0]][:ball_pos_a[1]]:
#             ball_a_flag = ball_a_flag and check(color)

#     ball_b_flag = True
#     if ball_pos_b[1] == 0:
#         ball_b_flag = True
#     else:
#         for color in A[ball_pos_b[0]][:ball_pos_b[1]]:
#             ball_b_flag = ball_b_flag and check(color)

#     # print(color, ball_a_flag, ball_b_flag)
#     return ball_a_flag and ball_b_flag





# if __name__ == "__main__":
#     main()
