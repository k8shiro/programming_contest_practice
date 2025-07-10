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
    S, T, X = map(int, stdin.readline().strip().split())

    if S <= T:
        if S <= X < T:
            print("Yes")
        else:
            print("No")
    else:  # S > T
        if S <= X < 24 or 0 <= X < T:
            print("Yes")
        else:
            print("No")

if __name__ == "__main__":
    main()
