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
    if 1 <= N <= 125:
        print(4)
    elif 126 <= N <= 211:
        print(6)
    elif 212 <= N <= 214:
        print(8)
 

if __name__ == "__main__":
    main()
