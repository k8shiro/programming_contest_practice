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
    A = list(map(int, stdin.readline().strip().split()))

    sum_a = sum(A)
    if sum_a <= M:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()
