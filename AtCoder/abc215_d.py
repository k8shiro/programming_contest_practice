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
    N, M = map(int, stdin.readline().split())
    A = list(map(int, stdin.readline().split()))

    factors = set()
    from sympy import factorint
    for a in A:
        _factors = factorint(a)
        # _factorsをsetに変換してから結合はTLEになるのでloopで追加
        for f in _factors:
            factors.add(f)
    factors = sorted(factors)
    # print(factors)

    gcd_1 = [True] * (M + 1)
    gcd_1[0] = False  # 0は除外
    for f in factors:
        for num in range(f, M + 1, f):
            gcd_1[num] = False
    # print(gcd_1)

    print(len([i for i in gcd_1 if i]))
    for idx, check in enumerate(gcd_1):
        if check:
            print(idx)

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
#     N, M = map(int, stdin.readline().split())
#     A = list(map(int, stdin.readline().split()))

#     factors = set()
#     from sympy import factorint
#     for a in A:
#         _factors = factorint(a)
#         factors = factors | set(_factors.keys())
#     factors = sorted(factors)
#     # print(factors)

#     gcd_1 = set([i for i in range(1, M + 1)])
#     # print(gcd_1)
#     for f in factors:
#         num = f
#         while num <= M:
#             if num in gcd_1:
#                 gcd_1.remove(num)
#             num += f
#     # print(gcd_1)

#     print(len(gcd_1))
#     for n in gcd_1:
#         print(n)

# if __name__ == "__main__":
#     main()
