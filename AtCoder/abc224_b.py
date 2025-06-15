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
    H, W = map(int, stdin.readline().strip().split())
    A = []
    for _ in range(H):
        a = list(map(int, stdin.readline().strip().split()))
        A.append(a)

    for i1 in range(H):
        for i2 in range(i1 + 1, H):
            for j1 in range(W):
                for j2 in range(j1 + 1, W):
                    if A[i1][j1] + A[i2][j2] > A[i1][j2] + A[i2][j1]:
                        print("No")
                        return
    print("Yes")

    




if __name__ == "__main__":
    main()
