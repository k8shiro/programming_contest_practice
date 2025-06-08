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
    X = int(stdin.readline().strip())
    if X == 0:
        print('No')
        return

    if X % 100 == 0:
        print('Yes')
    else:
        print('No') 

    




if __name__ == "__main__":
    main()
