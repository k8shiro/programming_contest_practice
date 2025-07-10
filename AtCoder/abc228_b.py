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
    N, X = map(int, stdin.readline().strip().split())
    A = list(map(int, stdin.readline().strip().split()))


    SEACRET = [0] * (N + 1)
    SEACRET[X] = 1
    while True:
        if SEACRET[A[X - 1]] == 1:
            break

        SEACRET[A[X - 1]] = 1
        X = A[X - 1]

    ans = sum(SEACRET)
    print(ans)

if __name__ == "__main__":
    main()
