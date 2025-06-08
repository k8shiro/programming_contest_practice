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

    S_LIST = [S]
    S_SHIFT = S
    while True:
        S_SHIFT = S_SHIFT[1:] + S_SHIFT[0]
        if S_SHIFT == S:
            break
        S_LIST.append(S_SHIFT)

    S_LIST.sort()
    ans1 = S_LIST[0]
    ans2 = S_LIST[-1]

    print(ans1)
    print(ans2)

    




if __name__ == "__main__":
    main()
