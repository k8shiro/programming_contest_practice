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
    A_set = set()
    for _ in range(N):
        A = list(map(int, stdin.readline().strip().split()))
        A = tuple(A)
        A_set.add(A)

    print(len(A_set))





if __name__ == "__main__":
    main()
