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
    X, Y = map(int, stdin.readline().strip().split())

    bento = []
    for _ in range(N):
        a, b = map(int, stdin.readline().strip().split())
        bento.append((a, b))
    
    dp = [[INT_MAX] * (Y + 1) for _ in range(X + 1)]
    dp[0][0] = 0

    ANS = INT_MAX
    for a, b in bento:
        # 逆順に更新（0-1ナップサック）
        for i in range(X, -1, -1):
            for j in range(Y, -1, -1):
                ni = min(X, i + a)
                nj = min(Y, j + b)
                dp[ni][nj] = min(dp[ni][nj], dp[i][j] + 1)



    ans = dp[X][Y]
    print(ans if ans != INT_MAX else -1)


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
#     X, Y = map(int, stdin.readline().strip().split())

#     bento = []
#     for _ in range(N):
#         a, b = map(int, stdin.readline().strip().split())
#         bento.append((a, b))
    
#     dp = [set() for _ in range(N + 1)] 
#     dp[0].add((0, 0))  # 初期状態は何も選ばない

#     ANS = INT_MAX
#     for a, b in bento:
#         for n in range(N-1, -1, -1):
#             for sum_a, sum_b in dp[n]:
#                 if sum_a + a >= X and sum_b + b >= Y:   
#                     ANS = min(ANS, n + 1)
#                 elif sum_a + a >= X:
#                     if (X, sum_b + b) not in dp[n + 1]:
#                         dp[n + 1].add((X, sum_b + b))
#                 elif sum_b + b >= Y:
#                     if (sum_a + a, Y) not in dp[n + 1]:
#                         dp[n + 1].add((sum_a + a, Y))
#                 else:
#                     if (sum_a + a, sum_b + b) not in dp[n + 1]:
#                         dp[n + 1].add((sum_a + a, sum_b + b))

#     # print(dp)

#     if ANS == INT_MAX:
#         print(-1)
#     else:
#         print(ANS)


# if __name__ == "__main__":
#     main()
