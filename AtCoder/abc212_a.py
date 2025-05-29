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
    A, B = map(int, stdin.readline().split())

    if 0 < A and B == 0:
        print("Gold")
    elif A == 0 and 0 < B:
        print("Silver")
    elif 0 < A and 0 < B:
        print("Alloy")


if __name__ == "__main__":
    main()
