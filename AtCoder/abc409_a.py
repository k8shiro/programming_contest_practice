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
    T = str(stdin.readline().strip())
    A = str(stdin.readline().strip())

    for t, a in zip(T, A):
        if t == 'o' and a == 'o':
            print('Yes')
            return
    print('No')

    




if __name__ == "__main__":
    main()
