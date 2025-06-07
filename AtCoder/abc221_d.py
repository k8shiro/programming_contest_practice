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

    LOGIN_OUT = []
    for _ in range(N):
        A, B = map(int, stdin.readline().strip().split())
        LOGIN_OUT.append((A, 1))
        LOGIN_OUT.append((A+B, -1))

    LOGIN_OUT.sort()

    counter = 0
    day = 1
    ANS = [0] * (N + 1)
    # print(LOGIN_OUT)

    for d, inout in LOGIN_OUT:
        if d != day:
            ANS[counter] += d - day
            day = d

        counter += inout
    
    print(*ANS[1:])

if __name__ == "__main__":
    main()
