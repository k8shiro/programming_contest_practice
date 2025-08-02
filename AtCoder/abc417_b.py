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
    A = list(map(int, stdin.readline().split()))
    B = list(map(int, stdin.readline().split()))

    B.sort()
    a_idx = 0
    b_idx = 0
    while a_idx < N and b_idx < M:
        if A[a_idx] == B[b_idx]:
            A[a_idx] = -1
            a_idx += 1
            b_idx += 1
        elif A[a_idx] < B[b_idx]:
            a_idx += 1
        else:
            b_idx += 1

    ans = [a for a in A if a != -1]
    if len(ans) == 0:
        return
    else:
        print(*ans)
    


if __name__ == "__main__":
    main()
