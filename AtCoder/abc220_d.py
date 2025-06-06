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
    N = int(stdin.readline().strip())
    A = list(map(int, stdin.readline().strip().split()))

    dp = [[0] * 10 for _ in range(N)]
    dp[0][A[0]] = 1

    idx = 0
    for a in A[1:]:
        idx += 1
        for i in range(10):
            dp[idx][(i * a) % 10] += dp[idx - 1][i] % MOD
            dp[idx][(i + a) % 10] += dp[idx - 1][i] % MOD

    for ans in dp[-1]:
        print(ans % MOD)





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


# MOD = 998244353

# def main():
#     global ANS
#     N = int(stdin.readline().strip())
#     A = list(map(int, stdin.readline().strip().split()))
#     solve(A[0], 1, A)
#     for ans in ANS:
#         print(ans)

# ANS = [0] * 10
# def solve(top, idx, A):
#     global ANS
#     if idx == len(A):
#         ANS[top] += 1
#         ANS[top] %= MOD
#         return top

#     solve((top + A[idx]) % 10, idx + 1, A)
#     solve((top * A[idx]) % 10, idx + 1, A)





# if __name__ == "__main__":
#     main()
