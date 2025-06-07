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
    N, L = map(int, stdin.readline().strip().split())
    D = list(map(int, stdin.readline().strip().split()))

    if L % 3 != 0:
        print(0)
        return
    hen = L // 3

    POINT = [0] * L
    p = 0
    POINT[0] = 1
    for d in D:
        p += d
        p %= L
        POINT[p] += 1

    ans = 0
    # print(hen)
    # print(POINT)
    for idx in range(hen):
        if POINT[idx] > 0 and POINT[hen + idx] > 0 and POINT[2 * hen + idx] > 0:
            # print(idx, hen + idx, 2 * hen + idx)
            ans += POINT[idx] * POINT[hen + idx] * POINT[2 * hen + idx]

    print(ans)
    




if __name__ == "__main__":
    main()