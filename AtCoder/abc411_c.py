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
    N, Q = map(int, stdin.readline().strip().split())
    A = list(map(int, stdin.readline().strip().split()))

    masu = [1] * (N + 2) # 1が白 -1が黒
    count = 0
    for a in A:
        masu[a] *= -1
        if masu[a-1] == 1 and masu[a] == 1 and masu[a+1] == 1:
            count -= 1
        elif masu[a-1] == -1 and masu[a] == -1 and masu[a+1] == -1:
            count -= 1
        elif masu[a-1] == 1 and masu[a] == -1 and masu[a+1] == 1:
            count += 1
        elif masu[a-1] == -1 and masu[a] == 1 and masu[a+1] == -1:
            count += 1
        print(count)









if __name__ == "__main__":
    main()
