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
    N, M = map(int, stdin.readline().split())
    L = []
    R = []
    for _ in range(M):
        l, r = map(int, stdin.readline().split())
        L.append(l)
        R.append(r)
    L.sort()
    R.sort()

    # print(L)
    # print(R)

    KABE = [0] * (N + 1)
    for l in L:
        KABE[l - 1] += 1
    for r in R:
        KABE[r] -= 1
    
    # print(KABE)
    KABE_BOUGYO = []
    bougyo = 0
    for k in KABE:
        bougyo += k
        KABE_BOUGYO.append(bougyo)
    # print(KABE_BOUGYO)

    ans = min(KABE_BOUGYO[:-1])
    print(ans)
        




if __name__ == "__main__":
    main()
