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
    S1 = str(stdin.readline().strip())
    S2 = str(stdin.readline().strip())

    if S1 == '#.' and S2 == '.#':
        print('No')
        return
    if S1 == '.#' and S2 == '#.':
        print('No')
        return
    print('Yes')


if __name__ == "__main__":
    main()
