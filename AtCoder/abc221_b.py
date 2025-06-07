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
    S = str(stdin.readline().strip())
    T = str(stdin.readline().strip())

    if S == T:
        print("Yes")
        return

    for i in range(1, len(S)):
        _S = S[:i-1] + S[i] + S[i-1] + S[i+1:]
        if _S == T:
            print("Yes")
            return
    print("No")


if __name__ == "__main__":
    main()
