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
    N, H, M = map(int, stdin.readline().strip().split())
    MONSTERS = []
    for _ in range(N):
        a, b = map(int, stdin.readline().strip().split())
        MONSTERS.append((a, b))

    DP = [[-1] * (M + 1) for _ in range(N + 1)]
    DP[0][M] = H
    ANS = 0
    for i, (a, b) in enumerate(MONSTERS):
        for j in range(M + 1):
            if DP[i][j] == -1:
                continue
            # HPを使う場合
            if DP[i][j] >= a:
                DP[i + 1][j] = max(DP[i + 1][j], DP[i][j] - a)
                ANS = max(ANS, i + 1)
            # MPを使う場合
            if j >= b:
                DP[i + 1][j - b] = max(DP[i + 1][j - b], DP[i][j])
                ANS = max(ANS, i + 1)
    print(ANS)


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
#     N, H, M = map(int, stdin.readline().strip().split())
#     MONSTERS = []
#     for _ in range(N):
#         a, b = map(int, stdin.readline().strip().split())
#         MONSTERS.append((a, b))

#     from collections import deque
#     queue = deque([(H, M)])
#     log = set()
#     log.add((H, M, 0))

#     ans_count = 0
#     for a, b in MONSTERS:
#         new_queue = deque()
#         while queue:
#             h, m = queue.popleft()
#             if h >= a and (h-1, m) not in log:
#                 new_queue.append((h - a, m))
#                 log.add((h - a, m, ans_count+1))
#             if m >= b and (h, m-1) not in log:
#                 new_queue.append((h, m - b))
#                 log.add((h, m - b, ans_count+1))
#         queue = new_queue
#         if queue:
#             ans_count += 1
    
#     print(ans_count)





# if __name__ == "__main__":
#     main()
