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
    N, W = map(int, stdin.readline().strip().split())

    cheese = []
    for _ in range(N):
        a, b = map(int, stdin.readline().strip().split())
        cheese.append((a, b))

    cheese.sort(reverse=True)
    #print(cheese)
    OISHISA = 0
    SUM_W = 0
    for a, b in cheese:
        if SUM_W + b >= W:
            OISHISA += a * (W - SUM_W)
            break
        else:
            OISHISA += a * b
            SUM_W += b

    print(OISHISA)


if __name__ == "__main__":
    main()
