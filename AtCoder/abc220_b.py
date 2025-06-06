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
    K = int(stdin.readline().strip())
    A, B = map(str, stdin.readline().strip().split())

    A10 = 0
    for a in A:
        A10 = A10 * K + int(a)

    B10 = 0
    for b in B:
        B10 = B10 * K + int(b)

    print(A10 * B10)

if __name__ == "__main__":
    main()
