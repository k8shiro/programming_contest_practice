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
    A, B, C = map(int, stdin.readline().strip().split())
    ANS = (B // C) * C
    if A <= ANS <= B:
        print(ANS)
    else:
        print(-1)



 

if __name__ == "__main__":
    main()
