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
    N, S = map(int, stdin.readline().split())
    T = list(map(int, stdin.readline().split()))

    TYORO = 0 + S + 0.5
    for t in T:
        if TYORO < t:
            print("No")
            return
        else:
            TYORO = t + S + 0.5
    
    print("Yes")

if __name__ == "__main__":
    main()
