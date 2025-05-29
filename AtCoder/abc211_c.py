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

CHOKUDAI_IDX = {
    0: "c",
    1: "h",
    2: "o",
    3: "k",
    4: "u",
    5: "d",
    6: "a",
    7: "i",
}

def main():
    S = str(stdin.readline().strip())

    DP = [[0] * 8 for _ in range(len(S))]

    for i in range(len(S)):
        s = S[i]
        for j in range(8):
            if i == 0:
                if s == "c" and j == 0:
                    DP[i][j] = 1
                else:
                    DP[i][j] = 0
            else:
                if s == "c" and j == 0:
                    DP[i][j] = (DP[i-1][j] + 1) % MOD
                elif s == CHOKUDAI_IDX[j]:
                    DP[i][j] = (DP[i-1][j-1] + DP[i-1][j]) % MOD
                else:
                    DP[i][j] = DP[i-1][j]
    
    print(DP[-1][-1])


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

# CHOKUDAI_NEXT = {
#     "c": "h",
#     "h": "o",
#     "o": "k",
#     "k": "u",
#     "u": "d",
#     "d": "a",
#     "a": "i",
# }

# def main():
#     S = str(stdin.readline().strip())
#     ANS = dfs(S, 0, '')
#     print(ANS)
    
# @lru_cache(maxsize=None)
# def dfs(S, idx, CHOKUDAI=''):
#     if CHOKUDAI == "chokudai":
#         return 1

#     if idx >= len(S):
#         return 0

#     ans = 0
#     # idxをCHOKUDAIに追加するか追加しないで再帰
#     if len(CHOKUDAI) == 0:
#         if S[idx] == 'c':
#             ans += dfs(S, idx + 1, CHOKUDAI + S[idx]) % MOD
#     else:
#         if S[idx] == CHOKUDAI_NEXT[CHOKUDAI[-1]]:
#             ans += dfs(S, idx + 1, CHOKUDAI + S[idx]) % MOD
#     ans += dfs(S, idx + 1, CHOKUDAI) % MOD
#     return ans % MOD

# if __name__ == "__main__":
#     main()