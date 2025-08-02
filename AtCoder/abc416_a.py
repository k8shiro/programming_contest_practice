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
    N, L, R = map(int, stdin.readline().split())
    S = str(stdin.readline().strip())
    for i in range(L, R+1):
        if S[i-1] == 'o':
            continue
        else:
            print('No')
            return
    print('Yes')


if __name__ == "__main__":
    main()
