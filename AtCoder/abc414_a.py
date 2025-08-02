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
    ans = 0
    for _ in range(N):
        x, y = map(int, stdin.readline().split())
        if x <= L and y >= R:
            ans += 1

    print(ans)

    


if __name__ == "__main__":
    main()
