
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
A = []
B = []
def main():
    global A, B
    N = int(stdin.readline().strip())
    A = list(map(int, stdin.readline().strip().split()))
    B = list(map(int, stdin.readline().strip().split()))

    dp = [ [0] * (3000 + 1) for _ in range(N + 1) ]

    for c in range(A[0], B[0] + 1):
        dp[0][c] = 1
    for idx in range(1, N):
        for c in range(A[idx], B[idx] + 1):
            if c == A[idx]:
                dp[idx][c] = sum(dp[idx - 1][:c+1]) % MOD
            else:
                dp[idx][c] = (dp[idx][c - 1] + dp[idx - 1][c]) % MOD
    #print(dp)
    ans = sum(dp[N - 1][A[N - 1]:B[N - 1] + 1]) % MOD
    print(ans)


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

# MOD = 998244353
# A = []
# B = []
# def main():
#     global A, B
#     N = int(stdin.readline().strip())
#     A = list(map(int, stdin.readline().strip().split()))
#     B = list(map(int, stdin.readline().strip().split()))

#     ans = solve(0, 0)
#     print(ans % MOD)



# @lru_cache(None)
# def solve(idx, pre):
#     global A, B
#     if idx == len(A):
#         return 1

#     ret = 0
#     for i in range(A[idx], B[idx] + 1):
#         if i >= pre:
#             ret += solve(idx + 1, i)
#             ret %= MOD
#     return ret % MOD


# if __name__ == "__main__":
#     main()
