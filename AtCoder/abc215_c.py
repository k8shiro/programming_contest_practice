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
    S, K = map(str, stdin.readline().split())
    K = int(K)

    S = list(S)
    import itertools
    perms = list(itertools.permutations(S))

    from sortedcontainers import SortedSet
    ss = SortedSet([])

    for p in perms:
        ss.add(''.join(p))

    print(ss[K-1])

if __name__ == "__main__":
    main()
