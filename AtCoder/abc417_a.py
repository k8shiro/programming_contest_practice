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
    N, A, B = map(int, stdin.readline().split())
    S = str(stdin.readline().strip())
    if B == 0:
        ans = S[A:]
    else:
        ans = S[A:-1*B]
    print(ans)
    


if __name__ == "__main__":
    main()
