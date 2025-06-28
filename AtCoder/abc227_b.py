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
    S = list(map(int, stdin.readline().strip().split()))

    s_set = set()
    for a in range(1, 1000+1):
        for b in range(1, 1000+1):
            s = 4*a*b + 3*a + 3*b
            s_set.add(s)

    count = 0
    for s in S:
        if not s in s_set:
            count += 1

    print(count)


if __name__ == "__main__":
    main()
